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
package org.fedai.osx.broker.util;

import org.fedai.osx.api.constants.Protocol;
import org.fedai.osx.broker.grpc.ContextPrepareInterceptor;
import org.fedai.osx.core.context.FateContext;

public class ContextUtil {

    public static FateContext buildFateContext(Protocol protocol) {
        FateContext context = new FateContext();
        context.setProtocol(protocol);
        context.setSourceIp(ContextPrepareInterceptor.sourceIp.get() != null ? ContextPrepareInterceptor.sourceIp.get().toString() : "");

        return context;
    }


}
