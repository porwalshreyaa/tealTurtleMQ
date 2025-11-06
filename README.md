# tealTurtleMQ

    Producer (server)    - posts request with topic name and event/msg data -> Broker (server)


    if queue/topic doesn't exist:
        Broker creates new queue/topic

    else:
        adds event/msg to queue/topic if it exists

    - Producer (server)   <- returns response of event/msg added to queue - Broker (server)


    Broker stores the queue in the disk to keep it safe even when broker itself fails

    Broker (server)    - sends event/msg -> Consumer (server)

        till it doesn't get confirmation it keeps trying while exponential delay and (if no reception) after some time stops
        
        Rather, it sends the event/msg to DLQ (dead letter queue)



    Broker (server)   <- if received consumer responds with acknowlwdgement of reception of event/msg - Consumer (server)

    - once confirmed reception broker then removes event/msg from disk and queue 