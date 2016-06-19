#!/usr/bin/python
# Title: jsonHandle.py
# Description: Contains all sort of operations with JSON objects
# Author: Sawan J. Kapai Harpalani
# Date: 2016-06-17
# Version: 0.1
# Usage: python jsonHandle.py
# Notes: 
# python_version: 2.6.6
# License: Copyright 200X Sawan J. Kapai Harpalani 
# This file is part of MMOTracker. MMOTracker is free software: you can redistribute it  and/or modify 
# it under the terms of the GNU GeneralPublic License as published by the Free Software  Foundation, 
# either version 3 of the License,  or (at your option) any later version 
# MMOTracker is distributed in the hope that it willbe useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESSFOR A PARTICULAR PURPOSE. See the GNU General 
# PubliLicense for more details.You should have received a copy of the GNU GeneralPublic License along with MMOTracker. 
# If not, seehttp://www.gnu.org/licenses/.
#==============================================================================

import json

# Constants
DEFAULT_IDENTATION = 4
DEFAULT_DELIMITATOR = '__'
BLANK = 'NULL'

# Creates a json object from a string
def stringToJSON(jsonString):
	return json.loads(jsonString)

# Transform json object to string
def jsonToString(jsonObject):
	return json.dumps(jsonObject)

# prints json object in a pretty way
def printJSON(jsonObject, indentationValue = DEFAULT_IDENTATION):
	print json.dumps(jsonObject, indent = indentationValue, sort_keys = True)

# Removes levels of the json object, returning a flat object
def flattenJSON(jsonObject, delim = DEFAULT_DELIMITATOR):
    result = {}
    for i in jsonObject.keys():
        if isinstance( jsonObject[i], dict ):
            get = flattenJSON( jsonObject[i], delim )
            for j in get.keys():
                result[ i + delim + j ] = get[j]
        else:
            result[i] = jsonObject[i]
    return result

# Check if the object contains elements of the same size
def checkSize(jsonObjectList):
    sizeFirst = len(jsonObjectList[0].keys()) 
    for item in jsonObjectList:
        if sizeFirst != len(item.keys()):
            return False
    return True

# Converts to string
def toString(s):
    try:
        return str(s)
    except:
        return s.encode('utf-8')

# Reduces elements
def reduceElement(key, value):
    global reducedElement
    
    if type(value) is list:
        i = 0
        for subElement in value:
            reduceElement(key + '_' + toString(i), subElement)
            i = i + 1
    elif type(value) is dict:
        subKeys = value.keys()
        for subKey in subKeys:
            reduceElement(key + '_' + toString(subKey), value[subKey])
    else:
        reducedElement[toString(key)] = toString(value)

# Returns a list with all the different headers that the JSON object contains
def getHeaders(jsonObjectList):
    headersList = []
    for json in jsonObjectList:
        for key in json.keys():
            if key not in headersList:
                headersList.append(key)
    return headersList

# Returns a list with the content ready to write in CSV
def getData(jsonObjectList, headerList):
    dataList = []
    for json in jsonObjectList:
        row = []
        for header in headerList:
            if header in json.keys():
                row.append(json[header])
            else:
                row.append(BLANK)
        dataList.append(row)
    return dataList
        # for key, value in json.iteritems():
        #      print("key: {} | value: {}".format(key, value))
            # print content.key()