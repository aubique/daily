import su.litvak.chromecast.api.v2.Application;
import su.litvak.chromecast.api.v2.ChromeCast;
import su.litvak.chromecast.api.v2.ChromeCasts;
import su.litvak.chromecast.api.v2.Status;

import java.io.IOException;
import java.security.GeneralSecurityException;

public class TestChrome {

    public TestChrome() {
        try {
            ChromeCasts.startDiscovery();
            Thread.sleep(10000);
        } catch (InterruptedException | IOException e) {
            e.printStackTrace();
        }

        ChromeCast cs = ChromeCasts.get().get(0);

        try {
            cs.connect();
            System.out.println(cs.getStatus().toString());
            cs.disconnect();
        } catch (IOException | GeneralSecurityException e) {
            e.printStackTrace();
        }

        try {
            ChromeCasts.stopDiscovery();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public TestChrome(int nul) {
        try {
            ChromeCasts.startDiscovery();
            ChromeCast cs = new ChromeCast("192.168.1.24");
            cs.connect();
            Status status = cs.getStatus();
            System.out.println(status.toString());
            if (cs.isAppAvailable("CC1AD845") && !status.isAppRunning("CC1AD845")) {
                Application app = cs.launchApp("CC1AD845");
            }
//            cs.load("Big Buck Bunny",           // Media title
//                    "images/BigBuckBunny.jpg",  // URL to thumbnail based on media URL
//                    "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", // media URL
//                    null // media content type (optional, will be discovered automatically)
//            );
            cs.load("https://download-s.akamaihd.net/fle/EygcBzup66GAvYymmRf6sRBqKUYsFzBmPVoPwHyHwUuhx2RBuZEQT068sWjVKiZrxwTSz70VnDnitLfwm_1_fle.mp4?__token__=exp=1583410022~hmac=1d2f4fe273dcb5cbc3f46da49b39f7ebf31f9da9ceaea1efe307285f0eccc9e3");
//            cs.load("https://wol.jw.org/ru/wol/mp/r2/lp-u/w19/2019/915");
//            cs.load("https://download-a.akamaihd.net/files/media_publication/ca/sjjm_U_054_r720P.mp4");
//            cs.play();
//            cs.seek(2237);
//            Thread.sleep(10000);
//            cs.stopApp();
//            cs.disconnect();
        } catch (IOException e) {
            System.out.println("Failed to discover");
            e.printStackTrace();
            throw new RuntimeException();
        } catch (GeneralSecurityException e) {
            System.out.println("Failed to connect");
            e.printStackTrace();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
        }
    }
}
