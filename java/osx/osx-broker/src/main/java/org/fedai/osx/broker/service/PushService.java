/*
 * Copyright 2019 The FATE Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fedai.osx.broker.service;

import com.webank.ai.eggroll.api.networking.proxy.Proxy;
import io.grpc.stub.StreamObserver;
import org.fedai.osx.broker.ServiceContainer;
import org.fedai.osx.broker.grpc.QueuePushReqStreamObserver;
import org.fedai.osx.core.config.MetaInfo;
import org.fedai.osx.core.context.FateContext;
import org.fedai.osx.core.exceptions.ExceptionInfo;
import org.fedai.osx.core.exceptions.SysException;
import org.fedai.osx.core.service.AbstractServiceAdaptor;
import org.fedai.osx.core.service.InboundPackage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PushService extends AbstractServiceAdaptor<FateContext,StreamObserver, StreamObserver> {

    Logger logger = LoggerFactory.getLogger(PushService.class);


    
    @Override
    protected StreamObserver doService(FateContext context, InboundPackage<StreamObserver> data
    ) {

        StreamObserver backRespSO = data.getBody();
       // context.setNeedPrintFlowLog(false);
        QueuePushReqStreamObserver queuePushReqStreamObserver = new QueuePushReqStreamObserver(context,
                ServiceContainer.routerRegister.getRouterService(MetaInfo.PROPERTY_FATE_TECH_PROVIDER),
                backRespSO, Proxy.Metadata.class);
        return queuePushReqStreamObserver;
    }

    @Override
    protected StreamObserver transformExceptionInfo(FateContext context, ExceptionInfo exceptionInfo) {
        logger.error("PushService error {}", exceptionInfo);
        throw new SysException(exceptionInfo.toString());
    }
}
