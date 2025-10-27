# tealTurtleMQ

Producer (server)   - post request with topic name and event/msg data -> Broker (server)

Broker creates new queue/topic if it doesn't exist, adds event/msg to queue/topic if it exists

Producer (server)   <- returns response of event/msg added to queue - Broker (server)

Broker stores the queue in the disk to keep it safe even when broker itself fails

Broker (server)   - sends event/msg -> Consumer (server)

till it doesn't get confirmation it keeps trying but slows down the process and after some time stops sending for some cool down period even after trying too much if no reception it sends the event/msg to DLQ

Broker (server)   <- if received consumer responds with acknowlwdgement of reception of event/msg - Consumer (server)

once confirmed reception broker then removes event/msg from disk and queue 