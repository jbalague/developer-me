import urllib.request
import urllib.error
import json
import argparse


def tellSparkDo(action):
    try:
        request = urllib.request.Request(
            url=action['url'], 
            method=action['method'], 
            headers=action['headers'], 
            data=json.dumps(action['data']).encode('utf-8'))
        response = urllib.request.urlopen(request)
        data = json.loads(response.read())
    except Exception as error:
        data = {'error': error}
    finally:
        return(data)


def sendMessageToRoom(message, roomId): 
    return(
        {
            'url': 'https://api.ciscospark.com/v1/messages',
            'method': 'POST',
            'headers': HEADERS,
            'data': {
                'roomId': roomId,
                'text': message
            }
        }
    )

def getListOfRooms():
    return(
        {
            'url': 'https://api.ciscospark.com/v1/rooms',
            'method': 'GET',
            'headers': HEADERS,
            'data': {}
        }
    )

def parseArguments(parser):
    parser.description = 'Cisco Spark utility.'
    parser.add_argument('access_token', metavar='TOKEN',
                        help='access token to validate access and indentity')
    parser.add_argument('-s', '--send',
                        action='store_true', dest='action_send_message',
                        default=False,
                        help='send a message to a room')
    parser.add_argument('--room', 
                        action='store', dest='room_id',
                        help='room id of the room where ')
    parser.add_argument('--text', 
                        action='store', dest='message',
                        help='the message that will sent')
    parser.add_argument('-lr',
                        action='store_true', dest='action_list_rooms',
                        default=False,
                        help='get the list rooms')
    parser.add_argument('-v',
                        action='store_true', dest='verbose',
                        default=False,
                        help='show response from server')
    return(parser.parse_args())
    
    
parser = argparse.ArgumentParser()
args = parseArguments(parser)

HEADERS = {
    'Content-type': 'application/json; charset=utf-8',
    'Authorization': 'Bearer ' + args.access_token
}

# Get the list of rooms
if args.action_list_rooms:
    
    print('Getting the list of rooms...')
    listOfRooms = tellSparkDo(getListOfRooms())
    if 'error' not in listOfRooms:
        print()
        print('1-to-1 rooms')
        print('-' * 100)
        for room in listOfRooms['items']:
            if room['type'] == 'direct':
                print('  - {} --> {}'.format(room['title'], room['id']))
        
        print()
        print('Group rooms')
        print('-' * 100)
        for room in listOfRooms['items']:
            if room['type'] == 'group':
                print('  - {} --> {}'.format(room['title'], room['id']))
        
        if args.verbose:
            print(json.dumps(listOfRooms))
        
    else:
        print('Oops! Something went wrong: {}'.format(listOfRooms['error']))


# Send a message to a room
elif args.action_send_message and \
     args.room_id is not None and \
     args.message is not None:

    print('Sending the message...')
    result = tellSparkDo(sendMessageToRoom(args.message, args.room_id))
    if 'error' not in result:
        print('Done!')
        if args.verbose:
            print(json.dumps(result))

    else:
        print('Oops! Something went wrong: {}'.format(result['error']))

# Show usage
else:
    parser.print_help()