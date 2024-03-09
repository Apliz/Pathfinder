from flask import Flask, current_app as app, json
from databases import db
# File to store all helper functions

# Functions in alphabetical order
################################
# 1. json_decode()
    # Takes stringified JSON and returns decoded json object
# 2. orbitalBodiesSQLINSERT
    # inserts celestrack JSON data into orbitalBodies.db
    # Removes logic from db.py
# 3. baz()
################################

def json_decode(data) :
  decoded_json = data.decode('utf8').replace('"','"')
  data = json.loads(decoded_json)
  return data

def orbitalBodiesSQLInsert(characteristic, count, db):
  db.execute("""
            INSERT INTO orbitalBodies(
                id,
                objectname,
                objectid,
                epoch,
                mean_motion,
                eccentricity,
                inclination,
                ra_ascending_node,
                arg_pericenter,
                mean_anomaly,
                ephemeris_type,
                classification_type,
                norad_cat_id,
                element_set_no,
                revolution_no,
                bstar,
                mean_motion_dot,
                mean_motion_ddot
            ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )""",(   
                count,
                characteristic["OBJECT_NAME"],
                characteristic["OBJECT_ID"],
                characteristic["EPOCH"],
                float(characteristic["MEAN_MOTION"]),
                float(characteristic["ECCENTRICITY"]),
                float(characteristic["INCLINATION"]),
                float(characteristic["RA_OF_ASC_NODE"]),
                float(characteristic["ARG_OF_PERICENTER"]),
                float(characteristic["MEAN_ANOMALY"]),
                int(characteristic["EPHEMERIS_TYPE"]),
                characteristic["CLASSIFICATION_TYPE"],
                int(characteristic["NORAD_CAT_ID"]),
                int(characteristic["ELEMENT_SET_NO"]),
                int(characteristic["REV_AT_EPOCH"]),
                float(characteristic["BSTAR"]),
                int(characteristic["MEAN_MOTION_DOT"]),
                int(characteristic["MEAN_MOTION_DDOT"]),
            ))