# Replace <YOUR ACCESS TOKEN GOES HERE> with your Cisco SPark Access Token
export SPARK_ACCESS_TOKEN=<YOUR ACCESS TOKEN GOES HERE>

# Replace <ONE ROOM ID> with one particular Cisco Spark Room ID
export SPARK_ROOM_ID=<ONE ROOM ID>

# # Get list of rooms 
# curl -s https://api.ciscospark.com/v1/rooms \
# -H "Authorization: Bearer $SPARK_ACCESS_TOKEN"

# Get room details
curl -vs "https://api.ciscospark.com/v1/rooms/$SPARK_ROOM_ID" \
-H "Authorization: Bearer $SPARK_ACCESS_TOKEN"

# # Send a message to a room
# curl -vs https://api.ciscospark.com/v1/messages \
# -X POST \
# -H 'Content-type: application/json; charset=utf-8' \
# -H "Authorization: Bearer $SPARK_ACCESS_TOKEN"
# -d '{"roomId":"$SPARK_ROOM_ID","text":"Go minions!"}'

