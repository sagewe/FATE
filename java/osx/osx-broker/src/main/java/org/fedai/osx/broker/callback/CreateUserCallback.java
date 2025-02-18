package org.fedai.osx.broker.callback;

import org.fedai.osx.broker.ServiceContainer;
import org.fedai.osx.broker.consumer.GrpcEventHandler;
import org.fedai.osx.broker.message.MessageExt;
import org.fedai.osx.broker.queue.TransferQueue;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CreateUserCallback  implements MsgEventCallback{

    Logger logger = LoggerFactory.getLogger(CreateUserCallback.class);
    public  CreateUserCallback(Class  eventHandlerClass){
        this.grpcEventHandlerClass = eventHandlerClass;

    }
    Class  grpcEventHandlerClass ;

    @Override
    public  void callback(TransferQueue queue , MessageExt message) {
            String topic = queue.getTransferId();
            if(ServiceContainer.consumerManager.getEventDrivenConsumer(topic)==null){
                GrpcEventHandler grpcEventHandler = null;
                try {
                    grpcEventHandler = (GrpcEventHandler)grpcEventHandlerClass.newInstance();
                } catch (InstantiationException e) {
                    throw new RuntimeException(e);
                } catch (IllegalAccessException e) {
                    throw new RuntimeException(e);
                }
                ServiceContainer.consumerManager.createEventDrivenConsumer(topic,grpcEventHandler);
            };
    }

}
