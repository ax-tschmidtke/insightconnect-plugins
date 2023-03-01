# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Perform an IP address lookup"


class Input:
    GETASN = "getAsn"
    IPADDRESS = "ipAddress"
    

class Output:
    RESULTS = "results"
    

class IpLookupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "getAsn": {
      "type": "boolean",
      "title": "Get ASN",
      "description": "Whether to return ASN information",
      "order": 2
    },
    "ipAddress": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address for which information will be searched",
      "order": 1
    }
  },
  "required": [
    "getAsn",
    "ipAddress"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IpLookupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/ipAddressObject",
      "title": "Results",
      "description": "Results containing information about the given IP address",
      "order": 1
    }
  },
  "definitions": {
    "asEventActor": {
      "type": "object",
      "title": "asEventActor",
      "properties": {
        "eventAction": {
          "type": "string",
          "title": "Event Action",
          "description": "The reason for the event",
          "order": 1
        },
        "eventDate": {
          "type": "string",
          "title": "Event Date",
          "description": "The time and date the event occurred",
          "order": 2
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "asEventActor": {
          "type": "array",
          "title": "As Event Actor",
          "description": "As event actor",
          "items": {
            "$ref": "#/definitions/asEventActor"
          },
          "order": 9
        },
        "entities": {
          "type": "array",
          "title": "Entities",
          "description": "Entities",
          "items": {
            "type": "object"
          },
          "order": 5
        },
        "events": {
          "type": "array",
          "title": "Events",
          "description": "Events",
          "items": {
            "$ref": "#/definitions/event"
          },
          "order": 8
        },
        "handle": {
          "type": "string",
          "title": "Handle",
          "description": "The registry-unique identifier of the entity",
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 7
        },
        "objectClassName": {
          "type": "string",
          "title": "Object Class Name",
          "description": "The type of object being processed",
          "order": 1
        },
        "port43": {
          "type": "string",
          "title": "Port 43",
          "description": "The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found",
          "order": 11
        },
        "publicIds": {
          "type": "array",
          "title": "Public IDs",
          "description": "List of public IDs",
          "items": {
            "$ref": "#/definitions/publicId"
          },
          "order": 4
        },
        "remarks": {
          "type": "array",
          "title": "Remarks",
          "description": "Information about the object class",
          "items": {
            "$ref": "#/definitions/notice"
          },
          "order": 6
        },
        "roles": {
          "type": "array",
          "title": "Roles",
          "description": "List of roles",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "status": {
          "type": "array",
          "title": "Status",
          "description": "The state of the entity",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      },
      "definitions": {
        "asEventActor": {
          "type": "object",
          "title": "asEventActor",
          "properties": {
            "eventAction": {
              "type": "string",
              "title": "Event Action",
              "description": "The reason for the event",
              "order": 1
            },
            "eventDate": {
              "type": "string",
              "title": "Event Date",
              "description": "The time and date the event occurred",
              "order": 2
            }
          }
        },
        "event": {
          "type": "object",
          "title": "event",
          "properties": {
            "eventAction": {
              "type": "string",
              "title": "Event Action",
              "description": "The reason for the event",
              "order": 1
            },
            "eventActor": {
              "type": "string",
              "title": "Event Actor",
              "description": "The actor responsible for the event",
              "order": 2
            },
            "eventDate": {
              "type": "string",
              "title": "Event Date",
              "description": "The time and date the event occurred",
              "order": 3
            }
          }
        },
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 4
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Rel",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 1
            }
          }
        },
        "notice": {
          "type": "object",
          "title": "notice",
          "properties": {
            "description": {
              "type": "array",
              "title": "Description",
              "description": "Description",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "links": {
              "type": "array",
              "title": "Links",
              "description": "Links",
              "items": {
                "$ref": "#/definitions/link"
              },
              "order": 3
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 1
            }
          },
          "definitions": {
            "link": {
              "type": "object",
              "title": "link",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "description": "Href",
                  "order": 4
                },
                "rel": {
                  "type": "string",
                  "title": "Rel",
                  "description": "Rel",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type",
                  "order": 3
                },
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Value",
                  "order": 1
                }
              }
            }
          }
        },
        "publicId": {
          "type": "object",
          "title": "publicId",
          "properties": {
            "identifier": {
              "type": "string",
              "title": "Identifier",
              "description": "The public identifier of the type related to 'type'",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The type of public identifier",
              "order": 1
            }
          }
        }
      }
    },
    "event": {
      "type": "object",
      "title": "event",
      "properties": {
        "eventAction": {
          "type": "string",
          "title": "Event Action",
          "description": "The reason for the event",
          "order": 1
        },
        "eventActor": {
          "type": "string",
          "title": "Event Actor",
          "description": "The actor responsible for the event",
          "order": 2
        },
        "eventDate": {
          "type": "string",
          "title": "Event Date",
          "description": "The time and date the event occurred",
          "order": 3
        }
      }
    },
    "ipAddressObject": {
      "type": "object",
      "title": "ipAddressObject",
      "properties": {
        "ansCountryCode": {
          "type": "string",
          "title": "ASN Country Code",
          "description": "ASN country code",
          "order": 3
        },
        "ansRegistry": {
          "type": "string",
          "title": "ASN Registry",
          "description": "ASN registry",
          "order": 6
        },
        "asn": {
          "type": "string",
          "title": "ASN",
          "description": "ASN",
          "order": 1
        },
        "asnCidr": {
          "type": "string",
          "title": "ASN CIDR",
          "description": "ASN CIDR",
          "order": 2
        },
        "asnDate": {
          "type": "string",
          "title": "ASN Date",
          "description": "ASN date",
          "order": 4
        },
        "asnDescription": {
          "type": "string",
          "title": "ASN Description",
          "description": "ASN description",
          "order": 5
        },
        "country": {
          "type": "string",
          "title": "Country",
          "description": "The two-character country code of the network",
          "order": 15
        },
        "endAddress": {
          "type": "string",
          "title": "End Address",
          "description": "The ending IP address of the network, either IPv4 or IPv6",
          "order": 11
        },
        "entities": {
          "type": "array",
          "title": "Entities",
          "description": "Information of organizations, corporations, governments, non-profits, clubs, individual persons, and informal groups of people",
          "items": {
            "$ref": "#/definitions/entity"
          },
          "order": 20
        },
        "events": {
          "type": "array",
          "title": "Events",
          "description": "List of events that have occurred",
          "items": {
            "$ref": "#/definitions/event"
          },
          "order": 18
        },
        "handle": {
          "type": "string",
          "title": "Handle",
          "description": "The RIR-unique identifier of the network registration",
          "order": 9
        },
        "ipVersion": {
          "type": "string",
          "title": "IP Version",
          "description": "The IP protocol version of the network, 'v4' signifies an IPv4 network, and 'v6' signifies an IPv6 network",
          "order": 12
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 19
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The identifier assigned to the network registration by the registration holder",
          "order": 13
        },
        "notices": {
          "type": "array",
          "title": "Notices",
          "description": "Information about the service providing RDAP information and/or information about the entire response",
          "items": {
            "$ref": "#/definitions/notice"
          },
          "order": 8
        },
        "objectClassName": {
          "type": "string",
          "title": "Object Class Name",
          "description": "The type of object being processed",
          "order": 23
        },
        "parentHandle": {
          "type": "string",
          "title": "Parent Handle",
          "description": "The RIR-unique identifier of the parent network of this network registration",
          "order": 16
        },
        "port43": {
          "type": "string",
          "title": "Port 43",
          "description": "The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found",
          "order": 21
        },
        "rdapConformance": {
          "type": "array",
          "title": "RDAP Conformance",
          "description": "RDAP conformance",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "remarks": {
          "type": "array",
          "title": "Remarks",
          "description": "Information about the object class",
          "items": {
            "$ref": "#/definitions/notice"
          },
          "order": 17
        },
        "startAddress": {
          "type": "string",
          "title": "Start Address",
          "description": "The starting IP address of the network, either IPv4 or IPv6",
          "order": 10
        },
        "status": {
          "type": "array",
          "title": "Status",
          "description": "The state of the IP network",
          "items": {
            "type": "string"
          },
          "order": 22
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The RIR-specific classification of the network per that RIR's registration model",
          "order": 14
        }
      },
      "definitions": {
        "asEventActor": {
          "type": "object",
          "title": "asEventActor",
          "properties": {
            "eventAction": {
              "type": "string",
              "title": "Event Action",
              "description": "The reason for the event",
              "order": 1
            },
            "eventDate": {
              "type": "string",
              "title": "Event Date",
              "description": "The time and date the event occurred",
              "order": 2
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "asEventActor": {
              "type": "array",
              "title": "As Event Actor",
              "description": "As event actor",
              "items": {
                "$ref": "#/definitions/asEventActor"
              },
              "order": 9
            },
            "entities": {
              "type": "array",
              "title": "Entities",
              "description": "Entities",
              "items": {
                "type": "object"
              },
              "order": 5
            },
            "events": {
              "type": "array",
              "title": "Events",
              "description": "Events",
              "items": {
                "$ref": "#/definitions/event"
              },
              "order": 8
            },
            "handle": {
              "type": "string",
              "title": "Handle",
              "description": "The registry-unique identifier of the entity",
              "order": 2
            },
            "links": {
              "type": "array",
              "title": "Links",
              "description": "Links",
              "items": {
                "$ref": "#/definitions/link"
              },
              "order": 7
            },
            "objectClassName": {
              "type": "string",
              "title": "Object Class Name",
              "description": "The type of object being processed",
              "order": 1
            },
            "port43": {
              "type": "string",
              "title": "Port 43",
              "description": "The fully qualified host name or IP address of the WHOIS server where the containing object instance may be found",
              "order": 11
            },
            "publicIds": {
              "type": "array",
              "title": "Public IDs",
              "description": "List of public IDs",
              "items": {
                "$ref": "#/definitions/publicId"
              },
              "order": 4
            },
            "remarks": {
              "type": "array",
              "title": "Remarks",
              "description": "Information about the object class",
              "items": {
                "$ref": "#/definitions/notice"
              },
              "order": 6
            },
            "roles": {
              "type": "array",
              "title": "Roles",
              "description": "List of roles",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "status": {
              "type": "array",
              "title": "Status",
              "description": "The state of the entity",
              "items": {
                "type": "string"
              },
              "order": 10
            }
          },
          "definitions": {
            "asEventActor": {
              "type": "object",
              "title": "asEventActor",
              "properties": {
                "eventAction": {
                  "type": "string",
                  "title": "Event Action",
                  "description": "The reason for the event",
                  "order": 1
                },
                "eventDate": {
                  "type": "string",
                  "title": "Event Date",
                  "description": "The time and date the event occurred",
                  "order": 2
                }
              }
            },
            "event": {
              "type": "object",
              "title": "event",
              "properties": {
                "eventAction": {
                  "type": "string",
                  "title": "Event Action",
                  "description": "The reason for the event",
                  "order": 1
                },
                "eventActor": {
                  "type": "string",
                  "title": "Event Actor",
                  "description": "The actor responsible for the event",
                  "order": 2
                },
                "eventDate": {
                  "type": "string",
                  "title": "Event Date",
                  "description": "The time and date the event occurred",
                  "order": 3
                }
              }
            },
            "link": {
              "type": "object",
              "title": "link",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "description": "Href",
                  "order": 4
                },
                "rel": {
                  "type": "string",
                  "title": "Rel",
                  "description": "Rel",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type",
                  "order": 3
                },
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Value",
                  "order": 1
                }
              }
            },
            "notice": {
              "type": "object",
              "title": "notice",
              "properties": {
                "description": {
                  "type": "array",
                  "title": "Description",
                  "description": "Description",
                  "items": {
                    "type": "string"
                  },
                  "order": 2
                },
                "links": {
                  "type": "array",
                  "title": "Links",
                  "description": "Links",
                  "items": {
                    "$ref": "#/definitions/link"
                  },
                  "order": 3
                },
                "title": {
                  "type": "string",
                  "title": "Title",
                  "description": "Title",
                  "order": 1
                }
              },
              "definitions": {
                "link": {
                  "type": "object",
                  "title": "link",
                  "properties": {
                    "href": {
                      "type": "string",
                      "title": "Href",
                      "description": "Href",
                      "order": 4
                    },
                    "rel": {
                      "type": "string",
                      "title": "Rel",
                      "description": "Rel",
                      "order": 2
                    },
                    "type": {
                      "type": "string",
                      "title": "Type",
                      "description": "Type",
                      "order": 3
                    },
                    "value": {
                      "type": "string",
                      "title": "Value",
                      "description": "Value",
                      "order": 1
                    }
                  }
                }
              }
            },
            "publicId": {
              "type": "object",
              "title": "publicId",
              "properties": {
                "identifier": {
                  "type": "string",
                  "title": "Identifier",
                  "description": "The public identifier of the type related to 'type'",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "The type of public identifier",
                  "order": 1
                }
              }
            }
          }
        },
        "event": {
          "type": "object",
          "title": "event",
          "properties": {
            "eventAction": {
              "type": "string",
              "title": "Event Action",
              "description": "The reason for the event",
              "order": 1
            },
            "eventActor": {
              "type": "string",
              "title": "Event Actor",
              "description": "The actor responsible for the event",
              "order": 2
            },
            "eventDate": {
              "type": "string",
              "title": "Event Date",
              "description": "The time and date the event occurred",
              "order": 3
            }
          }
        },
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 4
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Rel",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 1
            }
          }
        },
        "notice": {
          "type": "object",
          "title": "notice",
          "properties": {
            "description": {
              "type": "array",
              "title": "Description",
              "description": "Description",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "links": {
              "type": "array",
              "title": "Links",
              "description": "Links",
              "items": {
                "$ref": "#/definitions/link"
              },
              "order": 3
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 1
            }
          },
          "definitions": {
            "link": {
              "type": "object",
              "title": "link",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "description": "Href",
                  "order": 4
                },
                "rel": {
                  "type": "string",
                  "title": "Rel",
                  "description": "Rel",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type",
                  "order": 3
                },
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Value",
                  "order": 1
                }
              }
            }
          }
        },
        "publicId": {
          "type": "object",
          "title": "publicId",
          "properties": {
            "identifier": {
              "type": "string",
              "title": "Identifier",
              "description": "The public identifier of the type related to 'type'",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The type of public identifier",
              "order": 1
            }
          }
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Href",
          "order": 4
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Rel",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 1
        }
      }
    },
    "notice": {
      "type": "object",
      "title": "notice",
      "properties": {
        "description": {
          "type": "array",
          "title": "Description",
          "description": "Description",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 1
        }
      },
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 4
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Rel",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            },
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Value",
              "order": 1
            }
          }
        }
      }
    },
    "publicId": {
      "type": "object",
      "title": "publicId",
      "properties": {
        "identifier": {
          "type": "string",
          "title": "Identifier",
          "description": "The public identifier of the type related to 'type'",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of public identifier",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)