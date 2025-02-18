package org.fedai.osx.broker.consumer;

import org.fedai.osx.broker.message.MessageExt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public  class EventDrivenConsumer extends LocalQueueConsumer  {

    Logger logger = LoggerFactory.getLogger(EventDrivenConsumer.class);
    GrpcEventHandler  eventHandler;
  //  Disruptor  disruptor;

    public EventDrivenConsumer(long consumerId, String topic,GrpcEventHandler eventHandler){

        super(consumerId,topic);
        this.eventHandler = eventHandler;
//        disruptor = new Disruptor(() -> new MessageEvent(),
//                16, DaemonThreadFactory.INSTANCE,
//                ProducerType.SINGLE, new BlockingWaitStrategy());
//        disruptor.handleEventsWith(eventHandler);
//        disruptor.start();

        logger.info("new EventDrivenConsumer {}",topic);

    }
//    public static final EventTranslatorOneArg<MessageEvent,MessageEvent> TRANSLATOR =
//            (event, sequence, arg) -> {
//                event.setTopic(arg.getTopic());
//                event.setDesPartyId(arg.getDesPartyId());
//                event.setSrcComponent(arg.getSrcComponent());
//                event.setSrcPartyId(arg.getSrcPartyId());
//                event.setDesComponent(arg.getDesComponent());
//                event.setSessionId(arg.getSessionId());
//            };

    public  void  fireEvent(MessageExt msg) throws Exception {
        //disruptor.publishEvent((EventTranslatorOneArg) TRANSLATOR,event);
        eventHandler.onEvent(msg);
    }


    @Override
    public void destroy() {


       // this.disruptor.shutdown();
    }


    public  static void main(String[] args){
//        MessageEvent  messageEvent = new MessageEvent();
//        EventDrivenConsumer  eventDrivenConsumer = new EventDrivenConsumer(0,"test",new MockDesGrpcEventHandler());
//        eventDrivenConsumer.fireEvent(messageEvent);

    }

}
