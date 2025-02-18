//package  org.fedai.osx.broker.ptp;
//
//import com.google.protobuf.Parser;
//import  org.fedai.osx.broker.ServiceContainer;
//import  org.fedai.osx.broker.grpc.QueueStreamBuilder;
//import  org.fedai.osx.broker.grpc.QueuePushReqStreamObserver;
//import  org.fedai.osx.broker.util.TransferUtil;
//import  org.fedai.osx.core.constant.TransferStatus;
//import  org.fedai.osx.core.context.Context;
//import  org.fedai.osx.core.exceptions.ExceptionInfo;
//import  org.fedai.osx.core.frame.GrpcConnectionFactory;
//import  org.fedai.osx.core.router.RouterInfo;
//import  org.fedai.osx.core.service.AbstractServiceAdaptor;
//import  org.fedai.osx.core.service.InboundPackage;
//import com.webank.ai.eggroll.api.networking.proxy.Proxy;
//import io.grpc.ManagedChannel;
//import io.grpc.stub.StreamObserver;
//import org.ppc.ptp.Osx;
//import org.ppc.ptp.PrivateTransferProtocolGrpc;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//
//public class PtpStreamTestService extends AbstractServiceAdaptor<StreamObserver, StreamObserver> {
//
//    Logger  logger = LoggerFactory.getLogger(PtpStreamTestService.class);
//    @Override
//    protected StreamObserver doService(Context context, InboundPackage<StreamObserver> data) {
//
//        return  new StreamObserver<Osx.Inbound>() {
//            TransferStatus  transferStatus = TransferStatus.INIT;
//            StreamObserver responseStreamObserver = data.getBody();
//            StreamObserver reqSb=null;
//            boolean  isDes = false;
//
////            private void initDes(Osx.Inbound first){
////
////
////                reqSb  =   HttpStreamBuilder.buildStream(responseStreamObserver,
////                        Osx.Outbound.parser(),
////                        GrpcConnectionFactory.createManagedChannel(context.getRouterInfo(),true),
////                        context.getSrcPartyId(),context.getDesPartyId(),context.getSessionId());
////                transferStatus =  TransferStatus.TRANSFERING;
////            }
//
//            private void initNotDes(Osx.Inbound first){
//                InboundPackage inboundPackage = new InboundPackage();
//                inboundPackage.setBody(first);
//                try {
//                    ServiceContainer.requestHandleInterceptor.doPreProcess(context, inboundPackage);
//                    ServiceContainer.routerInterceptor.doPreProcess(context,inboundPackage);
//                    logger.info("init========={}",context.getRouterInfo());
//                }catch (Exception e){
//                    e.printStackTrace();
//                }
//                logger.info("ppppppppppppppppppp {}",context.getRouterInfo());
//                reqSb  =   QueueStreamBuilder.createStreamFromOrigin(context,responseStreamObserver,
//                        Osx.Outbound.parser(),
//                        context.getRouterInfo(),
//                        context.getSrcPartyId(),
//                        context.getDesPartyId(),
//                        context.getSessionId(),null);
//                transferStatus =  TransferStatus.TRANSFERING;
//            }
//
//
//            @Override
//            public void onNext(Osx.Inbound inbound) {
//
////                if(isDes) {
////                    if (transferStatus == TransferStatus.INIT) {
////                        initDes(inbound);
////                    }
////                }
////                else{
//                    if(transferStatus==TransferStatus.INIT) {
//                        initNotDes(inbound);
//                    }
//               // }
//
//                if (reqSb != null) {
//                    reqSb.onNext(inbound);
//                }
//            }
//            @Override
//            public void onError(Throwable throwable) {
//                reqSb.onError(throwable);
//            }
//            @Override
//            public void onCompleted() {
//                logger.info("==============onCompleted==============");
//            }
//        };
//    }
//
//    @Override
//    protected StreamObserver transformExceptionInfo(Context context, ExceptionInfo exceptionInfo) {
//        return null;
//    }
//}
