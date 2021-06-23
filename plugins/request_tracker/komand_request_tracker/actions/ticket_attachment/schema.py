# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets the metadata and content of a specific attachment"


class Input:
    ATTACHMENT_ID = "attachment_id"
    TICKET_ID = "ticket_id"
    

class Output:
    CONTENT = "Content"
    CONTENTENCODING = "ContentEncoding"
    CONTENTTYPE = "ContentType"
    CREATED = "Created"
    CREATOR = "Creator"
    FILENAME = "Filename"
    HEADERS = "Headers"
    MESSAGEID = "MessageId"
    PARENT = "Parent"
    SUBJECT = "Subject"
    TRANSACTION = "Transaction"
    ID = "id"
    

class TicketAttachmentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachment_id": {
      "type": "integer",
      "title": "Attachment ID",
      "description": "Attachment ID e.g. 2",
      "order": 2
    },
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID e.g. 3",
      "order": 1
    }
  },
  "required": [
    "attachment_id",
    "ticket_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketAttachmentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "Content": {
      "type": "string",
      "title": "Content",
      "description": "Content",
      "order": 12
    },
    "ContentEncoding": {
      "type": "string",
      "title": "Content Encoding",
      "description": "Content encoding",
      "order": 10
    },
    "ContentType": {
      "type": "string",
      "title": "Content Type",
      "description": "Content type",
      "order": 9
    },
    "Created": {
      "type": "string",
      "title": "Created",
      "description": "Created",
      "order": 4
    },
    "Creator": {
      "type": "string",
      "title": "Creator",
      "description": "Creator",
      "order": 3
    },
    "Filename": {
      "type": "string",
      "title": "Filename",
      "description": "Filename",
      "order": 8
    },
    "Headers": {
      "type": "object",
      "title": "Headers",
      "description": "Headers",
      "order": 11
    },
    "MessageId": {
      "type": "string",
      "title": "Message ID",
      "description": "Message ID",
      "order": 7
    },
    "Parent": {
      "type": "integer",
      "title": "Parent",
      "description": "Parent",
      "order": 6
    },
    "Subject": {
      "type": "string",
      "title": "Subject",
      "description": "Subject",
      "order": 2
    },
    "Transaction": {
      "type": "integer",
      "title": "Transaction",
      "description": "Transaction",
      "order": 5
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "Id",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)