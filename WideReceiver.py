from Player import Player
import random

class WideReceiver(Player): 
    @classmethod
    def stat_metadata(cls) -> dict:
        return {
            #PHYSICAL 
            "height": {"mean": 72, "sd": 2}, #inches
            "weight": {"mean": 200, "sd": 10}, #pounds
            "speed": {"mean": 85, "sd": 2},
            "strength": {"mean": 70, "sd": 5},
            "quickness": {"mean": 80, "sd": 5},
            "jumping": {"mean": 85, "sd": 5}, 

            #DURABILITY 
            "health": {"mean": 100, "sd": 0},
            "stamina": {"mean": 90, "sd": 2}, 

            #TECHNICAL, QUARTERBACKING 
            "arm_strength": {"mean": 50, "sd": 10},
            "short_accuracy": {"mean": 35, "sd": 5},
            "med_accuracy": {"mean": 35, "sd": 5},
            "deep_accuracy": {"mean": 35, "sd": 5},
            "presnap_processing": {"mean": 35, "sd": 5},
            "postsnap_processing": {"mean": 35, "sd": 5},

            #TECHNICAL, RECEIVING  
            "route_running": {"mean": 80, "sd": 5},
            "catching": {"mean": 85, "sd": 5},
            "release": {"mean": 80, "sd": 5}, 

            #TECHNICAL, BALL-CARRYING
            "break_tackle": {"mean": 70, "sd": 5},
            "run_after_catch": {"mean": 80, "sd": 5},
            "vision": {"mean": 40, "sd": 5}, 

            #TECHNICAL, BLOCKING
            "gap_run_blocking": {"mean": 40, "sd": 5},
            "zone_run_blocking": {"mean": 40, "sd": 5},
            "pass_blocking": {"mean": 40, "sd": 5},
            "screen_blocking": {"mean": 40, "sd": 5},
            "stalk_blocking": {"mean": 60, "sd": 7},
            "crackback_blocking": {"mean": 60, "sd": 7},
            "lead_blocking": {"mean": 50, "sd": 5},
            #Refactor some of these into "open_field_blocking"?

            #TECHNICAL, PASS-RUSHING
            "speed_rush": {"mean": 30, "sd": 3}, 
            "power_rush": {"mean": 30, "sd": 3}, 
            "first_step": {"mean": 30, "sd": 3},

            #TECHNICAL, RUN-STOPPING
            "block_shedding": {"mean": 30, "sd": 3}, 
            "tackle": {"mean": 45, "sd": 5},

            #TECHNICAL, COVERAGE
            "press": {"mean": 40, "sd": 5}, 
            "man_coverage": {"mean": 40, "sd": 5}, 
            "zone_coverage": {"mean": 40, "sd": 5}, 
            "ball_skills": {"mean": 80, "sd": 5},

            #TECHNICAL, SPECIAL TEAMS 
            "kicking_power": {"mean": 30, "sd": 10},
            "kicking_accuracy": {"mean": 30, "sd": 10},
            "kick_returning": {"mean": 65, "sd": 7},
            "punting_power": {"mean": 30, "sd": 10},
            "punting_accuracy": {"mean": 30, "sd": 10},
            "punt_returning": {"mean": 65, "sd": 7},

            #MENTAL
            "awareness": {"mean": 70, "sd": 5}, #Higher = better play recognition
            "discipline": {"mean": 70, "sd": 5}, #Higher = fewer penalties and mental mistakes 
            "aggression": {"mean": 60, "sd": 5}, #Higher = deal more damage
            "grit": {"mean": 70, "sd": 5}, #Higher = less of a debuff when playing with low health/stamina 
            "leadership": {"mean": 55, "sd": 5}, #Higher = small stat buffs for teammates if player is a captain and has requisite perks
            "clutch": {"mean": 60, "sd": 5} #Higher = small stat buffs for self in key late-game situations
        }