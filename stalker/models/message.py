# -*- coding: utf-8 -*-
# Copyright (c) 2009-2013, Erkan Ozgur Yilmaz
# 
# This module is part of Stalker and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

from sqlalchemy import Column, Integer, ForeignKey
from stalker.models.entity import Entity
from stalker.models.mixins import StatusMixin

from stalker.log import logging_level
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging_level)

class Message(Entity, StatusMixin):
    """The base of the messaging system in Stalker
    
    Messages are one of the ways to collaborate in Stalker. The model of the
    messages is taken from the e-mail system. So it is pretty similiar to an
    e-mail message.
    
    :param from: the :class:`~stalker.models.user.User` object sending the
      message
    
    :param to: the list of :class:`~stalker.models.user.User`\ s to
      receive this message
    
    :param subject: the subject of the message
    
    :param body: the body of the message
    
    :param in_reply_to: the :class:`~stalker.models.message.Message`
      object which this message is a reply to.
    
    :param replies: the list of :class:`~stalker.models.message.Message`
      objects which are the direct replies of this message
    
    :param attachments: a list of
      :class:`~stalker.models.entity.SimpleEntity` objects attached to
      this message (so anything can be attached to a message)
    
    """
    __auto_name__ = True
    __tablename__ = "Messages"
    __mapper_args__ = {"polymorphic_identity": "Message"}
    message_id = Column("id", Integer, ForeignKey("Entities.id"),
                        primary_key=True)

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)