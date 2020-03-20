package dev.aubique;

import com.google.gson.Gson;
import lombok.Builder;
import lombok.Data;

public class Jar200317Json {

    public static void main(String[] args) {

        final ObjLevelTwo objTwo = ObjLevelTwo.builder()
                .id(1)
                .build();
        final ObjLevelOne objOne = ObjLevelOne.builder()
                .objectId(objTwo)
                .description("First item")
                .build();
        System.out.println(new Gson().toJson(objOne));
    }
}

@Data
@Builder
class ObjLevelOne {
    private ObjLevelTwo objectId;
    private String description;
}

@Data
@Builder
class ObjLevelTwo {
    private Integer id;
}
