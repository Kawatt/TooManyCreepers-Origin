import json
import os

creepers = [
    "badlands",
    "bamboo",
    "beach",
    "cave",
    "dark_oak",
    "desert",
    "dripstone",
    "hills",
    "jungle",
    "mushroom",
    "ocean",
    "savannah",
    "snowy",
    "spruce",
    "swamp"
]

os.makedirs("jsons", exist_ok=True)

for creeper in creepers:
    data = {
        "type": "apoli:action_on_entity_use",
        "bientity_action": {
            "type": "apoli:and",
            "actions": [
                {
                    "type": "apoli:target_action",
                    "action": {
                        "type": "apoli:execute_command",
                        "command": "tag @s add crepokwt.tp"
                    }
                },
                {
                    "type": "apoli:actor_action",
                    "action": {
                        "type": "apoli:and",
                        "actions": [
                            {
                                "type": "apoli:execute_command",
                                "command": f"origin set @s origins:origin crepokwt:{creeper}"
                            },
                            {
                                "type": "apoli:play_sound",
                                "sound": f"minecraft:entity.creeper.death"
                            },
                            {
                                "type": "apoli:execute_command",
                                "command": "tp @s @e[tag=crepokwt.tp,limit=1,sort=nearest]"
                            }
                        ]
                    }
                },
                {
                    "type": "apoli:target_action",
                    "action": {
                        "type": "apoli:and",
                        "actions": [
                            {
                                "type": "apoli:execute_command",
                                "command": "tp ~ -70 ~"
                            },
                            {
                                "type": "apoli:execute_command",
                                "command": "kill @s"
                            }
                        ]
                    }
                }
            ]
        },
        "bientity_condition": {
            "type": "apoli:target_condition",
            "condition": {
                "type": "apoli:and",
                "conditions": [
                    {
                        "type": "apoli:entity_type",
                        "entity_type": f"creeperoverhaul:{creeper}_creeper"
                    },
                    {
                        "type": "apoli:nbt",
                        "nbt": "{NoAI:1b}",
                        "inverted": True
                    }
                ]
            }
        }
    }

    with open(f"jsons/{creeper}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

print("JSONs generados correctamente.")