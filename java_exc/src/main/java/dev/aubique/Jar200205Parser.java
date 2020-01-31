import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.DomText;
import com.gargoylesoftware.htmlunit.html.HtmlDivision;
import com.gargoylesoftware.htmlunit.html.HtmlPage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * Parse fr.bab.la and output Json
 */
public class Jar200205Parser {

    static final String toFind = "pouvoir";
    static Map<String, Map<String, List<String>>> rows;
    static List<String> verbs = new ArrayList<>();

    static {
        rows = new TreeMap<>();
        verbs.add("pouvoir");
        verbs.add("aller");
        verbs.add("vouloir");
        verbs.add("connaitre");
        verbs.add("savoir");
        verbs.add("voir");
        verbs.add("dire");
        verbs.add("boire");
    }

    public static void main(String[] args) {
        for (String verb : verbs) {
            rows.put(verb, new BabLaParser200209(verb).parse());
        }
        try {
            // Output dictionary
            System.out.println(new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(rows));
        } catch (JsonProcessingException e) {
        }
    }

    private static class BabLaParser200209 {

        private final String BASE_URL = "https://fr.bab.la/conjugaison/francais/";
        private final String xpathInfinitive = "//div[@class=\'quick-result-entry\'][1]/div[@class=\'quick-result-overview\']/ul/li/text()";
        private final String xpathTense = "//h3[@class=\'conj-tense-block-header\'][text()=\'%s\']/../div";
        private HtmlPage page = null;
        private String targetVerb = "pouvoir";
        private String infinitive;
        private WebClient client = new WebClient();
        private Map<String, String> selectNames = new TreeMap<>();

        public BabLaParser200209(String verbToFind) {
            this.targetVerb = verbToFind;
            this.client.getOptions().setJavaScriptEnabled(false);
            this.client.getOptions().setCssEnabled(false);
            this.client.getOptions().setUseInsecureSSL(true);
            selectNames.put("Indicatif présent", "_pr");
            selectNames.put("Indicatif passé composé", "_pp");
            selectNames.put("Indicatif imparfait", "_im");
            selectNames.put("Indicatif futur", "_fu");
        }

        public Map<String, List<String>> parse() {
            Map<String, List<String>> dict = new TreeMap<>();

            if (this.targetVerb.isEmpty()) {
                this.targetVerb = "pouvoir";
            }
            try {
                this.page = this.client.getPage(this.BASE_URL + this.targetVerb);
                this.infinitive = ((DomText) page.getFirstByXPath(this.xpathInfinitive)).getTextContent();
//            System.out.println(infinitive);
                selectNames.entrySet().stream()
                        //this.dict.put(infinitive + dict-value, listTenseContent(dict-key));
                        .forEach(e -> dict.put(this.infinitive + e.getValue(), getSixForms(e.getKey())));
            } catch (IOException e) {
                e.printStackTrace();
            }

            return dict;
        }

        private List<String> getSixForms(String key) {
            List<String> tenseContent = new ArrayList<>();
//        System.out.println();
            List<HtmlDivision> divs = this.page.getByXPath(String.format(this.xpathTense, key));
            for (HtmlDivision div : divs) {
                DomText conjPerson = div.getFirstByXPath("div[@class=\'conj-person\']/text()");
                DomText conjResult = div.getFirstByXPath("div[@class=\'conj-result\']/text()");

                StringBuilder conjItem = new StringBuilder();
                conjItem.append(conjPerson.getTextContent());
                conjItem.append(" ");
                conjItem.append(conjResult.getTextContent());
//            System.out.println(conjItem.toString());
                tenseContent.add(conjItem.toString());
            }
            return tenseContent;
        }
    }
}
