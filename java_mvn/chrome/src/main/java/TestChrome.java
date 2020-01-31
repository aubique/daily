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
//            cs.load("https://download-s.akamaihd.net/fle/gWNZyEqXsdtcA6wiyqtBacjcV5APWeUQbDxpDkUpcuZBGtOuIbUdfCpyEsCqA48phENuhIB6yYf8zKZzW_1_fle.mp4?__token__=exp=1582408099~hmac=7f5ba82f5816e315b7b7705ec475b7311d4b3bb406a832bb59e6ddae07213de5");
            cs.load("https://upload.wikimedia.org/wikipedia/fr/d/d2/Sonic_Generations_Logo.jpg");
//            cs.play();
//            cs.seek(2237);
            Thread.sleep(10000);
            cs.stopApp();
            cs.disconnect();
        } catch (IOException e) {
            System.out.println("Failed to discover");
            e.printStackTrace();
            throw new RuntimeException();
        } catch (GeneralSecurityException e) {
            System.out.println("Failed to connect");
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
