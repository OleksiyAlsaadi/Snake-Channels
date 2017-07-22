import json

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session

from random import randint

from .models import *

sizex = 50;
sizey = 32;
inc = 0;
cell = [0] * sizex * sizey;
pelletx = sizex/2;
pellety = sizey/2;

# Connected to websocket.connect
@channel_session
def ws_connect(message):
    global inc;
    inc = 2;
    # Accept connection
    #room = Room.objects.get(label=label)
    message.reply_channel.send({"accept": True})
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Suggestion.objects.all().delete()
    Group("game-%s" % room).add(message.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    global inc, sizex, cell, pelletx, pellety;
    #inc += 1;
    if (inc > 0):
        inc -= 1;
    #x = message.content.get('text'[0])
    #message.reply_channel.send({"text":})

    suggestions = Suggestion.objects.all()
    #Suggestion.objects.all().delete()
    #add = Suggestion(suggestion=message['text'])
    #add.save()

    data = json.loads(message['text'])
    #print(data['name'])
    score = []
    board = []
    if (data['game'] == "snake"):

        if (data['eaten'] == 1):
            pelletx = randint(1,sizex-1)
            pellety = randint(1,sizey-1)
        #print(pellety);
        #cell[data['x']+data['y']*sizex] = 1;

        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]

        a = 0 #search for player name. If not found, add to database
        for n in range(len(suggest['suggestions'])):
            if (suggest['suggestions'][n]['suggestion'] == data['name']):
                a = 1;
                if (data['score'] != suggest['suggestions'][n]['id']):
                    Suggestion.objects.filter(suggestion=data['name']).delete()
                    a = 0;
                break;
        if (a == 0):
            add_player = Suggestion(suggestion=data['name'], id=data['score'])
            add_player.save()
            #add newly added player name to local database instance
            #added = Suggestion.objects.filter(suggestion=data['name'])
            #for suggestion in added:
            #    suggest['suggestions']+=[{
            #        'id':suggestion.id,
            #        'suggestion': suggestion.suggestion
            #        }]
        suggestions = Suggestion.objects.all()
        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]

        #print(suggest)
        #str1 = str(suggest)
        #print( suggest['suggestions'][1]['suggestion'] )
        #score = suggest['suggestions'][0]['suggestion']
        for n in range(len(suggest['suggestions'])):
            score.append( suggest['suggestions'][n]['id'] )
            board.append( suggest['suggestions'][n]['suggestion'] )
    #print(board)

    Group("game-%s" % message.channel_session['room']).send({
        "text": json.dumps({
            #"mx": message['x'],
            #"my": message['y']
            "mx": data['x'],
            "my": data['y'],
            "inc": inc,
            "board": board,
            "score": score,
            "player_score": data['score'],
            "cell": cell,
            "id": data['id'],
            "dir": data['dir'],
            "killed": data['killed'],

            "pelletx": pelletx, #data['pelletx'],
            "pellety": pellety, #data['pellety'],
        }),
        #"text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("game-%s" % message.channel_session['room']).discard(message.reply_channel)
