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
package org.fedai.osx.broker;


import org.fedai.osx.broker.consumer.ConsumerManager;
import org.fedai.osx.broker.eggroll.EventDriverMsgManager;
import org.fedai.osx.broker.grpc.PcpGrpcService;
import org.fedai.osx.broker.http.HttpClientPool;
import org.fedai.osx.broker.queue.TransferQueueManager;
import org.fedai.osx.broker.router.DefaultFateRouterServiceImpl;
import org.fedai.osx.broker.router.FateRouterService;
import org.fedai.osx.broker.router.RouterRegister;
import org.fedai.osx.broker.security.TokenGeneratorRegister;
import org.fedai.osx.broker.security.TokenValidatorRegister;
import org.fedai.osx.broker.server.OsxServer;
import org.fedai.osx.broker.service.TokenApplyService;
import org.fedai.osx.broker.token.DefaultTokenService;
import org.fedai.osx.broker.zk.CuratorZookeeperClient;
import org.fedai.osx.broker.zk.ZkConfig;
import org.fedai.osx.core.config.MetaInfo;
import org.fedai.osx.core.flow.ClusterFlowRuleManager;
import org.fedai.osx.core.flow.FlowCounterManager;
import org.fedai.osx.core.service.AbstractServiceAdaptor;
import org.fedai.osx.tech.provider.TechProviderRegister;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Map;

public class ServiceContainer {
    static public ConsumerManager consumerManager;
    static public TransferQueueManager transferQueueManager;
    static public FlowCounterManager flowCounterManager;
    static public OsxServer transferServer;
    static public Map<String, AbstractServiceAdaptor> serviceAdaptorMap = new HashMap<String, AbstractServiceAdaptor>();
    static public TokenApplyService tokenApplyService;
    static public ClusterFlowRuleManager clusterFlowRuleManager;
    static public DefaultTokenService defaultTokenService;
    static public CuratorZookeeperClient zkClient;
    //厂商注册
    static public TechProviderRegister techProviderRegister;
    static public EventDriverMsgManager eventDriverMsgManager;
    //Token校验器，用于双方token校验
    static public  TokenValidatorRegister  tokenValidatorRegister;
    //Token生成器注册，用于双方token校验
    static public TokenGeneratorRegister tokenGeneratorRegister;

    static public RouterRegister  routerRegister;


    static Logger logger = LoggerFactory.getLogger(ServiceContainer.class);

    public static void init() {
        flowCounterManager = createFlowCounterManager();
        clusterFlowRuleManager = createClusterFlowRuleManager();
        zkClient = createCuratorZookeeperClient();
        transferQueueManager = createTransferQueueManager();
        consumerManager = createTransferQueueConsumerManager();
        tokenApplyService = createTokenApplyService();
        transferServer = new OsxServer();
        defaultTokenService = createDefaultTokenService();
        tokenApplyService = createTokenApplyService();
        eventDriverMsgManager = createEventDriverMsgManager( consumerManager, transferQueueManager);
        techProviderRegister = createTechProviderRegister();
        tokenValidatorRegister = createTokenValidatorRegister();
        tokenGeneratorRegister = createTokenGeneratorRegister();
        routerRegister = createRouterRegister();
        HttpClientPool.initPool();
        if (!transferServer.start()) {
            logger.error("server start failed");
            System.err.println("server start failed");
            System.exit(-1);
        } else {

        };


    }


    private static RouterRegister createRouterRegister(){
        RouterRegister routerRegister = new RouterRegister();
        routerRegister.init();
        routerRegister.start();
        return  routerRegister;
    }

    private static TokenValidatorRegister createTokenValidatorRegister(){
        TokenValidatorRegister  tokenValidatorRegister = new TokenValidatorRegister();
        tokenValidatorRegister.init();
        tokenValidatorRegister.start();
        return  tokenValidatorRegister;
    }

    private static TokenGeneratorRegister  createTokenGeneratorRegister(){
        TokenGeneratorRegister  tokenGeneratorRegister = new TokenGeneratorRegister();
        tokenGeneratorRegister.init();
        tokenGeneratorRegister.start();
        return tokenGeneratorRegister;
    }


    private static EventDriverMsgManager createEventDriverMsgManager(ConsumerManager consumerManager,TransferQueueManager transferQueueManager){
        EventDriverMsgManager  eventDriverMsgManager = new EventDriverMsgManager(consumerManager,transferQueueManager);
        eventDriverMsgManager.init();
        eventDriverMsgManager.start();
        return eventDriverMsgManager;
    }


    public static TechProviderRegister createTechProviderRegister() {
        try {
            TechProviderRegister techProviderRegister = new TechProviderRegister();
            techProviderRegister.start();
            return techProviderRegister;
        }catch(Exception e){
            logger.error("tech provider create error",e);
        }
        return null;

    }

    public static PcpGrpcService createPcpGrpcService() {
        return new PcpGrpcService();
    }

    public static CuratorZookeeperClient createCuratorZookeeperClient() {
        if (MetaInfo.isCluster()) {
            ZkConfig zkConfig = new ZkConfig(MetaInfo.PROPERTY_ZK_URL, 5000);
            return new CuratorZookeeperClient(zkConfig);
        }
        return null;
    }

    public static TokenApplyService createTokenApplyService() {
        TokenApplyService tokenApplyService = new TokenApplyService();
        tokenApplyService.start();
        return tokenApplyService;
    }

    public static DefaultTokenService createDefaultTokenService() {
        return new DefaultTokenService();
    }

    public static ClusterFlowRuleManager createClusterFlowRuleManager() {
        return new ClusterFlowRuleManager();
    }

    static FlowCounterManager createFlowCounterManager() {
        FlowCounterManager flowCounterManager = new FlowCounterManager("transfer");
        flowCounterManager.startReport();
        return flowCounterManager;
    }

    static ConsumerManager createTransferQueueConsumerManager() {
        ConsumerManager consumerManager = new ConsumerManager();
        return consumerManager;
    }

    static FateRouterService createFateRouterService() {
        DefaultFateRouterServiceImpl fateRouterService = new DefaultFateRouterServiceImpl();
        fateRouterService.start();
        return fateRouterService;
    }

    static TransferQueueManager createTransferQueueManager() {
        TransferQueueManager transferQueueManager = new TransferQueueManager();
        return transferQueueManager;
    }




}
