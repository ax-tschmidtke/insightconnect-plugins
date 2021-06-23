# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return the history that Umbrella has seen for a given domain"


class Input:
    DOMAIN = "domain"
    TYPE = "type"
    

class Output:
    FEATURES = "features"
    RRS_TF = "rrs_tf"
    

class RrHistoryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "DNS Record",
      "description": "DNS record query type (A, NS, MX, TXT and CNAME are supported)",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RrHistoryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "features": {
      "type": "array",
      "title": "Features",
      "description": "Features",
      "items": {
        "$ref": "#/definitions/feature"
      },
      "order": 2
    },
    "rrs_tf": {
      "type": "array",
      "title": "Resource Records",
      "description": "RRS TF",
      "items": {
        "$ref": "#/definitions/resource_record"
      },
      "order": 1
    }
  },
  "required": [
    "features",
    "rrs_tf"
  ],
  "definitions": {
    "feature": {
      "type": "object",
      "title": "feature",
      "properties": {
        "age": {
          "type": "integer",
          "title": "Age",
          "description": "The day in days between now and the last request for this domain. This value is only useful if present. A low score helps isolate attack domains that are short-lived",
          "order": 3
        },
        "asns": {
          "type": "array",
          "title": "ASNs",
          "description": "List of ASN numbers the IPs are in",
          "order": 11
        },
        "asns_count": {
          "type": "integer",
          "title": "ASNs Count",
          "description": "Number of ASNs the IPs map to",
          "order": 12
        },
        "base_domain": {
          "type": "string",
          "title": "Base Domain",
          "description": "The base domain of the requested domain",
          "order": 1
        },
        "cname": {
          "type": "boolean",
          "title": "CNAME",
          "description": "Returns true if a CNAME record has been seen for this domain name",
          "order": 23
        },
        "country_codes": {
          "type": "array",
          "title": "Country Codes",
          "description": "List of country codes (ex: US, FR, TW) for the IPs the name maps to",
          "order": 9
        },
        "country_count": {
          "type": "integer",
          "title": "Country Count",
          "description": "Number of countries the IPs are hosted in",
          "order": 10
        },
        "div_rips": {
          "type": "number",
          "title": "Div Rips",
          "description": "The number of prefixes over the number of IPs",
          "order": 16
        },
        "ff_candidate": {
          "type": "boolean",
          "title": "FF Candidate",
          "description": "If the domain name looks like a candidate for fast flux. This does not necessarily mean the domain is in fast flux, but rather that the IP address the domain resolves to changes rapidly (or has changed rapidly)",
          "order": 24
        },
        "geo_distance_mean": {
          "type": "number",
          "title": "Geo Distance Mean",
          "description": "Mean distance between the geo median and each location, in kilometers",
          "order": 20
        },
        "geo_distance_sum": {
          "type": "number",
          "title": "Geo Distance Sum",
          "description": "Minimum sum of distance between locations, in kilometers",
          "order": 19
        },
        "is_subdomain": {
          "type": "boolean",
          "title": "Is Subdomain",
          "description": "Returns true if the requested domain is a subdomain of another",
          "order": 2
        },
        "locations": {
          "type": "array",
          "title": "Locations",
          "description": "List of geo coordinates (WGS84 datum, decimal format) the IPs are mapping to",
          "order": 17
        },
        "locations_count": {
          "type": "integer",
          "title": "Locations Count",
          "description": "Number of distinct geo coordinates the IPs are mapping to",
          "order": 18
        },
        "mail_exchanger": {
          "type": "boolean",
          "title": "Mail Exchanger",
          "description": "If an MX query for this domain name has been seen",
          "order": 22
        },
        "non_routable": {
          "type": "boolean",
          "title": "Non Routable",
          "description": "If one of the IPs is in a reserved, non-routable IP range",
          "order": 21
        },
        "prefixes": {
          "type": "array",
          "title": "Prefixes",
          "description": "List of network prefixes the IPs map to",
          "order": 13
        },
        "prefixes_count": {
          "type": "integer",
          "title": "Prefixes Count",
          "description": "Number of network prefixes the IPs map to",
          "order": 14
        },
        "rips": {
          "type": "integer",
          "title": "Rips",
          "description": "Number of IPs seen for the domain name",
          "order": 15
        },
        "rips_stability": {
          "type": "number",
          "title": "Rips Stability",
          "description": "1.0 divided by the number of times the set of IP addresses changed",
          "order": 25
        },
        "ttls_max": {
          "type": "integer",
          "title": "TTL Max",
          "description": "Maximum amount of time set that DNS records should be cached",
          "order": 5
        },
        "ttls_mean": {
          "type": "number",
          "title": "TTL Mean",
          "description": "Average amount of time set that DNS records should be cached",
          "order": 6
        },
        "ttls_median": {
          "type": "number",
          "title": "TTL Median",
          "description": "Median amount of time set that DNS records should be cached",
          "order": 7
        },
        "ttls_min": {
          "type": "integer",
          "title": "TTL Min",
          "description": "Minimum amount of time set that DNS records should be cached",
          "order": 4
        },
        "ttls_stddev": {
          "type": "number",
          "title": "TTL Standard Deviation",
          "description": "Standard deviation of the amount of time set that DNS records should be cached",
          "order": 8
        }
      },
      "required": [
        "base_domain",
        "is_subdomain"
      ]
    },
    "resource_record": {
      "type": "object",
      "title": "resource_record",
      "properties": {
        "class": {
          "type": "string",
          "title": "Class",
          "description": "DNS class type",
          "order": 5
        },
        "first_seen": {
          "type": "string",
          "title": "First Seen",
          "description": "Date when the domain was first seen to our DNS database",
          "order": 1
        },
        "last_seen": {
          "type": "string",
          "title": "Last Seen",
          "description": "Date when domain was last seen in our DNS database",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the domain",
          "order": 3
        },
        "rr": {
          "type": "string",
          "title": "RR",
          "description": "Resource record IP for the domain",
          "order": 7
        },
        "ttl": {
          "type": "integer",
          "title": "TTL",
          "description": "TTL of the domain",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Query type",
          "order": 6
        }
      },
      "required": [
        "first_seen",
        "last_seen"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)