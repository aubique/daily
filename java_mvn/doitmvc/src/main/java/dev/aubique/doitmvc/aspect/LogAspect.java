package dev.aubique.doitmvc.aspect;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.springframework.stereotype.Component;

@Component
public class LogAspect {

    public void beforeServiceMethodInvocation(JoinPoint jp) {
        System.out.println("Invocation of method " + jp.getSignature());
    }

    public Object aroundServiceMethodExecution(ProceedingJoinPoint pjp) throws Throwable {
        final long start = System.currentTimeMillis();
        final Object res = pjp.proceed();
        final long end = System.currentTimeMillis();
        System.out.println(new StringBuilder()
                .append("Execution of method ")
                .append(pjp.getSignature())
                .append(" took ")
                .append(end - start)
                .append("msec.")
                .toString());
        return res;
    }
}
