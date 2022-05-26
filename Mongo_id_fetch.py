import requests
import json
import sys

missingIDs = 'mongoids.txt'
url = "https://data.mongodb-api.com/app/data-qdybx/endpoint/data/beta/action/findOne"

try:
  with open(missingIDs,'r') as f:
    with open('output2.txt', 'w') as g:      
        for line in f:
          m_id = line.strip()

          payload = json.dumps({
          "collection": "companies",
          "database": "sample_training",
          "dataSource": "Cluster0",
          "filter": {
          "_id": { "$oid" : "$id$"},
 #        "_id": id1 
             }
          })

          payload = payload.replace("$id$",m_id)
          
          headers = {
              'Content-Type': 'application/json',
              'Access-Control-Request-Headers': '*',
              'api-key': 's9eUTIHy8rLjndo0kBi41iaYSQcHdOu9bxLXwBBgWWFTPDETjtpFcnSyF3kZDx'
          }
          response = requests.request("POST", url, headers=headers, data=payload)
       
          final_line = str(m_id)+"Ç"+str(response.text)+"\n"
          g.write (final_line)
except IOError:
  print('Error: File %s does not appear to exist.' % addressfile)

