# HDBapocalypse — Game Design Sketch

> A Fallout Shelter–style side-view management game. You don't run a vault. You run one HDB block,
> with its void deck, lifts, corridors, rubbish chutes and residents, when the dead start walking.

---

## 1. Core pitch

- **View:** a side-on cross-section of one HDB block, like Fallout Shelter. Each floor is a horizontal
  strip: a **lift lobby + staircase core** in the middle and **2–3 units** on each side, joined by the
  **common corridor**. The **void deck** is at the bottom and the **rooftop** (water tanks, lift motor room)
  is at the top.
- **Side panels:** an "Outside" map with the supermarket, park, school, Neighbourhood Police Centre
  and, later, more places you can send people to.
- **Loop:** each day has 4 phases (Morning / Afternoon / Evening / Night). You assign residents to
  jobs, meet their needs, react to the event generator, and send expeditions out. Survive as long as you can,
  or reach one of the late-game endings.

### Difficulty = block height

| Mode   | Storeys | Units/floor | Starting residents | What gets harder                                                       |
|--------|---------|-------------|--------------------|------------------------------------------------------------------------|
| Easy   | 8       | 2           | ~16–24             | Short stair climbs, low rooftop, easy to defend one void deck          |
| Normal | 12      | 2–3         | ~30–45             | Lift dependence starts to matter, the water pump is needed past floor ~10 |
| Hard   | 20      | 3           | ~60–90             | Long stair trips, water pressure fails on high floors, more mouths, more politics |

Height should be a real system, not just more of everything:
- **Stair cost:** with the lift out, every trip costs stamina according to how many floors it climbs.
  Ah Ma on the 17th floor can't come down to the void deck for food.
- **Water pressure:** when the booster pumps lose power, floors above the rooftop tank's gravity
  head get no water. You need to haul it up or run pumps from a generator.
- **Defence depth:** taller blocks have more floors you can give up and barricade to fall back on.

---

## 2. Timeline: the countdown (T-14 → T-7 random start)

The game starts on a random day between **T-14 and T-7** before the outbreak hits Singapore. The player
never sees the exact T-number, only signals. This is the **prep phase**, and it is the most "Singapore"
part of the game.

### Signal ladder: DORSCON-style alert colours

| Alert            | What the player sees                                                                                         |
|------------------|--------------------------------------------------------------------------------------------------------------|
| 🟢 Green          | Overseas news clips: "mystery illness in [region]". Uncle at the kopitiam says it's fake news.               |
| 🟡 Yellow         | Temperature screening at the MRT station. Telegram and WhatsApp group rumours (some true, some false).        |
| 🟠 Orange         | **Panic buying**: rice, Maggi mee, canned sardines, toilet paper. Supermarket stock drops and prices rise. Schools move to home-based learning. |
| 🔴 Red            | Circuit-breaker lockdown. Police on patrol. First "violent patient" reports from hospitals.                   |
| ⚫ Black (fiction) | Outbreak day. The **Public Warning System siren** sounds (the "Important Message" tone), not on the usual test day. |

### Prep-phase actions (cost money, time and social standing)
- **Stockpile** at the supermarket. Each trip competes with NPC panic buyers, and "kiasu" residents
  overbuy and hoard in their own unit.
- **Organise the block** through the **Residents' Committee (RC)**: hold a void deck meeting, start a
  block WhatsApp group, assign floor captains.
- **Prepare the household shelter** (the "bomb shelter" storeroom in newer flats): clear out the
  junk (old fan, CNY decorations, a dusty treadmill) and turn it into a safe room or quarantine room.
- **Fill buckets and bathtubs**, buy a gas cylinder for cooking, a power bank, a portable radio.
- **Relatives:** a resident's family from another estate asks to move in. More hands, more mouths.
- Choices made here change the starting state for the outbreak (stockpile level, morale, trust).

---

## 3. The block: spaces and what you can build

### 3.1 Units (2–3 per floor)
Each unit has a **flat type** that sets its capacity and how many build slots it has:

| Flat type   | Residents | Room slots | Notes                                    |
|-------------|-----------|------------|------------------------------------------|
| 2-room      | 1–2       | 1          | Often elderly singles; low on resources  |
| 3-room      | 2–4       | 2          | Common in older blocks                   |
| 4-room      | 3–5       | 3          | The standard family flat                 |
| 5-room/Exec | 4–6       | 4          | Rare. Rich in stuff, sometimes a helper's room |

Units start **owned by their families**. You can't repurpose a unit without the owners agreeing
(see *Politics*). Empty or abandoned units can be **converted**:

| Conversion            | Function                                                               | Unlocks            |
|-----------------------|------------------------------------------------------------------------|--------------------|
| Communal Kitchen      | Cooks raw food into meals. Has halal / vegetarian / general stations.  | Start              |
| Storeroom             | Raises the food and supply cap. A target for theft.                     | Start              |
| Sick Bay              | Treatment. Works best staffed by the nurse, polyclinic staff or a TCM sinseh. | Start        |
| Quarantine Room       | Uses a household shelter (steel door!). Holds suspected infected.       | Start              |
| Workshop              | Makes barricades, weapons and repairs from scrap.                       | Day ~5             |
| Radio Room            | Picks up broadcasts and contacts other blocks.                          | Day ~10            |
| Classroom             | Kids keep studying (morale) and train skills.                           | Day ~15            |
| Prayer / Quiet Room   | Sanity recovery. Multi-faith (surau corner, altar, prayer mat).        | Day ~10            |
| Corridor Garden       | Grows kangkong, chilli, pandan, sweet potato leaves, lime.              | Day ~7             |
| Battery Bank          | Stores power from rooftop solar or a generator.                        | Day ~25            |

### 3.2 Common areas (the block's "shared rooms")
- **Void deck:** the main entrance and the first defence line. Upgrade path: shutters → letterbox-wall
  barricade → kill-zone with bicycle/PMD barricades. It also holds **events**: a void deck wedding tentage
  becomes a field hospital, and a void deck funeral is where you mourn the dead (a big morale event).
- **Lift lobby & lift:** lifts need power. A lift that breaks (or gets a zombie trapped in it) is a whole
  event chain. You can **lock lifts at a floor** to cut off access.
- **Staircase:** a choke point. Every floor can be **barricaded**; barricaded floors cost more to
  move through, but they buy time.
- **Common corridor:** potted plants, shoe racks, bicycles. Clutter = barricade material, but it
  is also a fire risk and a hiding spot.
- **Rubbish chute:** you have to keep it working or **sanitation** falls. Zombies sometimes come *up*
  through the bin centre. You can seal it (lower risk, sanitation crashes) or keep it open.
- **Rooftop:** water tanks, a rain-harvesting tarp, solar panels (late game), a lookout/signal post, a
  **bamboo pole antenna**. Lightning is dangerous here during thunderstorms.
- **Bin centre / Bicycle bay / Linkway / Multi-storey carpark (MSCP):** perimeter spaces you can
  claim and fortify.

---

## 4. Resources

| Resource         | Source                                                      | Drains                                     |
|------------------|-------------------------------------------------------------|--------------------------------------------|
| 🍚 Food (raw)     | Stockpile, supermarket runs, corridor garden, wet market    | Cooked into meals, spoils in the heat       |
| 🍛 Meals          | Communal kitchen                                            | 2–3 per resident per day                     |
| 💧 Water          | Taps (PUB, until it cuts), rooftop tank, rain harvest, NEWater plant run | Drinking, cooking, hygiene           |
| ⚡ Power          | Grid (until it cuts), generator + diesel, solar, car batteries | Lifts, pumps, fridges, fans, radio        |
| 🩹 Medicine       | Pharmacy, polyclinic, police station first aid kits, TCM hall | Injuries, illness, infection delay        |
| 🔧 Scrap/Materials| Corridor clutter, karang guni stash, MSCP cars, school      | Barricades, weapons, repairs                 |
| 🗡️ Weapons        | See below                                                  | Durability loss                              |
| 😊 Morale         | Meals, festivals, sleep, the park, prayer, kopi             | Deaths, hunger, heat, noise, fights           |
| 🤝 Trust          | Fair decisions, keeping promises                            | Favouritism, executions, hoarding found       |
| 🧼 Sanitation     | Rubbish chute, water, cleaners                              | Waste, rain flooding, dead bodies              |

**Weapons, Singapore edition:** civilians basically have no guns, so most weapons are improvised:
mop and broom spears, **changkol** (hoe), **parang** from a Malay neighbour's kitchen, cleavers from the
kopitiam, rattan canes, golf clubs, PMDs as rams, fire extinguishers. The **Neighbourhood Police Centre**
is the only reliable source of real gear (batons, shields, pepper spray, and a very rare locked armoury).
An **NSman** resident is better with any firearm you do find.

---

## 5. Residents

### 5.1 Stats: K.I.A.S.U.
| Stat               | Meaning                                       | Used for                               |
|--------------------|-----------------------------------------------|----------------------------------------|
| **K**ampung Spirit | Charisma and community                        | Morale jobs, negotiations, RC politics |
| **I**ntellect      | Problem solving                               | Radio, sick bay, workshop, classroom   |
| **A**gility        | Speed and stealth                             | Scavenging, running, stairs            |
| **S**trength       | Physical power                                | Barricades, combat, hauling water      |
| **U**lu Endurance  | Toughness and hunger/heat tolerance           | Long expeditions, illness resistance    |

### 5.2 Archetypes (generated with names, ages, languages and family links)
- **Ah Ma / Ah Gong:** low strength, high Kampung Spirit. Knows old remedies, remembers rationing from the
  Japanese Occupation, speaks only Hokkien or Teochew.
- **NSman (reservist):** combat bonus and good at drills. Gets call-up SMS events (does he report?).
- **NSF on book-out:** young and fit. Stuck outside camp when the outbreak hits.
- **Foreign Domestic Worker (helper):** high endurance and caregiving. Has her own family abroad
  and her own story arc. How the block treats her affects trust.
- **Migrant worker** (from the dorm nearby): strong, practical construction skills. Some residents
  are prejudiced against him, which creates a social conflict to manage.
- **Nurse / polyclinic staff:** sick bay bonus. Gets called back to the hospital.
- **Grab driver / delivery rider:** knows the roads, fast on expeditions, owns a vehicle.
- **Kopitiam uncle / hawker:** cooking bonus, feeds more people per raw unit.
- **Town council cleaner:** sanitation bonus, has keys to the bin centre and the rooftop.
- **RC auntie:** organisational bonus, knows everyone's business (gossip events).
- **Sec school students / JC students:** low stats but they learn fast. Mobile games keep morale up
  while there's power.
- **Karang guni man:** scrap bonus. His horn attracts zombies (risky!).
- **Ah Beng / Ah Lian:** combat and scavenging. Low obedience.
- **TCM sinseh / pharmacist / retired teacher / IT guy / insurance agent...**

### 5.3 Needs
Hunger, Thirst, Sleep, Heat Comfort (fans/aircon power!), Hygiene, Sanity, Social. Cultural needs give
the game texture and are handled respectfully:
- **Diet:** halal, vegetarian (some Hindus and Buddhists), no beef. The communal kitchen tracks this.
  Breaking it is a big trust hit for that family. Accommodating it costs efficiency.
- **Faith & ritual:** Friday prayers, Ramadan fasting (meal timings shift and stamina drops in the day),
  joss sticks (smoke = fire risk + zombie attraction), funerals done with proper rites.
- **Language:** mixed-language floors coordinate worse. Bilingual residents act as "translators".

### 5.4 Traits (generated, 1–3 per resident)
`Kiasu` (hoards, preps well), `Bo Chap` (doesn't care, calm, lazy), `Pantang` (superstitious, refuses
some tasks/days), `Chope King` (claims resources), `Sian` (low motivation), `Steady` (reliable),
`Kaypoh` (nosy, finds secrets), `Atas` (looks down on others, has nice stuff), `Sabo King` (sabotages
others), `Garang` (brave), `Pai Seh` (won't ask for help, hides wounds or bites!).

`Pai Seh` + bitten = a hidden infection. That is a key source of drama.

---

## 6. Infection & hard decisions

### Infection model
1. **Exposure** (scratch/bite on an expedition or a breach), sometimes **hidden** by traits.
2. **Incubation** (random 6–48 hrs). Symptoms: fever, irritability, sensitivity to light. A
   thermometer check (temperature screening returns!) can catch it early.
3. **Turn:** a breach event *inside* the block, on that resident's floor.

### Decision tree when someone is infected
- **Quarantine** in a household shelter (needs a guard and food, and the family visits).
- **Amputate** (scratch on a limb only, sick bay + skilled medic, chance to save them, permanent stat loss).
- **Experimental treatment** (late game: antiviral from the polyclinic or hospital, low odds).
- **Exile** (they leave. The family may leave too. Trust shifts).
- **Mercy** (huge morale and trust impact. Family may hold it against you, and the outcome depends
  on how the decision was made: alone, by RC vote, or by the family).

These are **social decisions** as much as survival ones. A **Trust** system remembers how you handled
similar cases before. If you were lenient with the RC chairman's son but harsh with the helper, the
block will notice.

---

## 7. Outside locations (expeditions)

Expeditions work like Fallout Shelter's wasteland: pick a team, choose supplies, pick a
**stance** (stealth / fast / thorough), and get a running log plus choice prompts.

| Location                         | Available | Loot / purpose                                    | Risks                                         |
|----------------------------------|-----------|---------------------------------------------------|-----------------------------------------------|
| **Supermarket** (next to block)  | Start     | Food, water, toiletries, batteries                 | Panic-buyer mobs early, looters later, cold-room horror |
| **Neighbourhood Park**           | Start     | Sanity recovery, fishing (pond), herbs, firewood  | Open ground, exposed at night                 |
| **Primary/Secondary School**     | Start     | Canteen supplies, science lab chemicals, first aid, uniform-group gear, **survivor kids & teachers** | Hall full of evacuees who turned |
| **Neighbourhood Police Centre**  | Start     | Batons, shields, radios, armoury (keycard), cells | Infected officers, locked doors               |
| Hawker Centre / Kopitiam         | Day ~5    | Gas cylinders, woks, rice, sauces                  | Fire, vermin                                   |
| Wet Market                       | Day ~5    | Fresh food (spoils fast), ice                      | Smell attracts hordes                          |
| Polyclinic                       | Day ~8    | Medicine, the antiviral chain                      | High infection density                        |
| Petrol Station                   | Day ~10   | Diesel/petrol for generators, snacks               | Explosions                                     |
| Multi-Storey Carpark             | Day ~10   | Car batteries, fuel siphoning, vehicles            | Darkness, dead ends                            |
| Community Club (CC)              | Day ~15   | Tables, chairs, PA system, function hall shelter   | Rival survivor group                           |
| MRT Station                      | Day ~20   | Tunnel routes between estates, CD shelter          | Tunnels are a maze                             |
| Neighbouring HDB block           | Day ~20   | Trade, alliance, or raid                           | Factions                                       |
| Condo down the road              | Day ~30   | Rich loot, gated security, pool (water!)           | Hostile "atas" survivors                       |
| Reservoir / NEWater plant        | Day ~40   | Water security                                     | Long trip                                      |
| SAF Camp                         | Day ~60   | Military gear, contact with the authorities        | Very high                                      |

---

## 8. Generative world systems

### 8.1 Weather (Singapore-accurate, varies by season)

| Weather              | Season / when                         | Effects                                                                                    |
|----------------------|---------------------------------------|--------------------------------------------------------------------------------------------|
| ☀️ Hot & humid       | Year round, worst Apr–Jun             | Heat need rises, food spoils faster, no fans = sanity drop, zombies slower at noon          |
| 🌧️ Afternoon thunderstorm | Inter-monsoon (Apr–May, Oct–Nov)  | Rain harvest, scent masking (stealth bonus), lightning on the rooftop, power surges         |
| 🌬️ Sumatra squall    | SW monsoon (Jun–Sep), predawn         | Sudden strong winds, rooftop damage, flying debris breaks barricades                        |
| 🌧️ Monsoon surge     | NE monsoon (Dec–Mar)                  | Days of rain, **flash floods** at the void deck/basement, sanitation crash, cooler (morale up) |
| 🌫️ Haze (PSI)        | ~Jun–Oct (Indonesian fires)           | PSI meter: high PSI = respiratory illness, N95 masks needed, **visibility drops for both you and the zombies** |
| 🌤️ Dry spell         | Feb–Mar                               | Rain tank runs low, water rationing                                                        |

### 8.2 Infrastructure decay (scripted ranges + random timing)
- **Power grid:** flickers → rolling blackouts → total failure (around day 10–25). Lifts, pumps and fridges stop.
- **Water (PUB):** pressure drops → taps on high floors fail → total failure (around day 15–30).
- **Telco:** mobile data dies, then SMS, and only radio is left.
- **Government broadcasts:** cut down to automatic loops, then go silent, then (late game) come back.

### 8.3 Zombie behaviour (the "threat director")
Something like the AI director in Left 4 Dead. It watches the block's **noise**, **light** and **smell**
scores and spawns pressure:
- Noise: generators, karang guni horns, getai, fights, gunshots, the PWS siren, a resident's alarm clock.
- Light: lit units at night (curtains/blackout tape needed).
- Smell: rubbish, bodies, cooking (durian = very bad idea, or a smart lure).
- **Horde events:** a void deck breach, a stairwell push, a lift shaft climb, the MSCP spilling over.
- **Zombie variants unlock over time:** the slow "uncle shuffler", the PMD-speed runner, the
  bloated (wet market) one, the "Ah Long" (debt collector, bangs on doors), and riot-gear zombies (from the
  police station).

### 8.4 Calendar & festivals (real dates drive events)
| Festival / date            | Event hook                                                                                   |
|----------------------------|----------------------------------------------------------------------------------------------|
| Chinese New Year           | Reunion dinner (big morale for a big food cost). Firecrackers: lure or disaster.             |
| Hari Raya Puasa / Ramadan  | Fasting changes meal timing. Open house = inter-floor trust boost.                           |
| Deepavali                  | Oil lamps (light at night, risky), sweets shared.                                             |
| Hungry Ghost Month (7th month) | Burning offerings (smoke + fire), getai noise, `Pantang` residents refuse night expeditions. Spooky "who is that in the corridor" events. |
| Total Defence Day (15 Feb) | PWS siren sounds by schedule. The ironic morale beat, plus it pulls hordes.                  |
| National Day (9 Aug)       | Rooftop flag raising, singing "Home" or "Count On Me Singapore" (morale ↑). Maybe a real fly-past = contact with the authorities. |
| Christmas / Vesak / Thaipusam | Smaller community events                                                                  |

---

## 9. Event / scenario generator (storylets)

Every event is a **storylet card** with tags, prerequisites, weight and outcomes, so content is
data-driven and new scenarios can be added without code.

```yaml
id: lift_trapped_auntie
title: "Auntie stuck in lift"
tags: [lift, power, rescue]
requires:
  power: flickering
  lift_working: true
weight: 3
cooldown_days: 6
prompt: >
  The power dips. Lift B stops between #09 and #10. Mdm Lim is inside with her groceries,
  and something is banging on the lift doors at #09.
choices:
  - text: "Send a team to pry the doors at #10"
    check: { stat: Strength, difficulty: 6, team: 2 }
    success: { morale: +5, trust: +3, gain: { food: 4 } }
    fail:    { injury: random_team_member, noise: +3 }
  - text: "Restart the lift from the motor room (needs cleaner's key)"
    requires: { resident_trait_or_role: town_council_cleaner }
    success: { power: -1, trust: +2 }
  - text: "Wait for power to stabilise"
    outcome: { roll: 50, good: "she's fine, just sian", bad: lift_horror_followup }
```

### Sample event pool (gets wider the longer you play)

**Day-to-day / domestic**
- Neighbour dispute over **corridor clutter** or **bamboo laundry poles** sticking out into the corridor.
- A **curry smell** complaint (a cultural-tolerance check).
- A family **hoarding** food in their household shelter, found by a `Kaypoh` resident.
- A kid's **PSLE** is coming. Do they keep studying? (The classroom pays off later.)
- A **community cat** shows up. Feeding it costs food, and it gives morale and an early warning of zombies.
- **Killer litter:** someone throws something off a high floor. Kills a zombie, or a resident.
- Someone wants to **smoke at the staircase** (fire risk, noise).
- The **aircon** argument: there's only enough power for one unit's aircon. Who gets it? Elderly? Babies?
- **Dengue** after rain (stagnant water in pots, so turn the pails over).

**Survival / crisis**
- The **rubbish chute** is blocked by... something.
- **Lightning** strikes the rooftop antenna.
- **Flash flood** in the void deck. Zombies float in.
- A **water tank** on the rooftop is contaminated (an infected body inside).
- A **pregnant resident** goes into labour at night.
- **Heatstroke** during a haze week with no power.

**Social / moral**
- Survivors from the **school** at the gate: 1 teacher, 6 kids. Food for 3 days.
- **Migrant workers** from the dorm ask for shelter. Residents are split.
- The **RC chairman** demands a bigger share as "leader".
- A resident wants to go **find her son** at another estate.
- An **NSman** gets an SMS mobilisation call-up. Report or stay?
- An infected resident's family **hides** them in their unit.

**Outside / world**
- A **radio** broadcast: an evacuation point at [location] in 3 days. True?
- **Another block** signals with torches at night. Ally or trap?
- **Looters** on motorbikes demand a "tax".
- **Condo survivors** offer to trade for your rooftop water.
- An **SAF helicopter** flies over. Signal it?

---

## 10. Progression: longer playthroughs unlock more to manage

The game grows in **layers**. Each layer adds a new management system on top of the ones you already have.

| Phase | Days        | Theme             | New systems unlocked                                                                                    |
|-------|-------------|-------------------|---------------------------------------------------------------------------------------------------------|
| 0     | T-14 → T-0  | **Kiasu Prep**    | Stockpiling, RC meetings, household shelter prep, relatives moving in                                   |
| 1     | 1 – 7       | **Lockdown**      | Void deck defence, expeditions (4 starting locations), basic needs, infection decisions                 |
| 2     | 8 – 30      | **Lights Out**    | Power and water collapse → generators, rainwater, stair logistics, corridor gardens, workshop, weather begins to bite |
| 3     | 31 – 60     | **Block Politics**| Unit conversion votes, rationing policy, crime and punishment, factions inside the block, the Trust system becomes central |
| 4     | 61 – 120    | **Estate Network**| Diplomacy and trade with other blocks, linkway/sky bridge building, shared defence, the radio network, MRT tunnel routes |
| 5     | 121 – 200   | **Town Council**  | Govern a whole precinct: assign blocks to roles (farm block, clinic block, armoury block), elect leaders |
| 6     | 200+        | **Endgame**       | Choose a path: **Evacuation** (to Pulau Tekong / a ship off Changi), **Cure** (the polyclinic → hospital lab chain), **Rebuild** (a new republic, "Majulah") |

### Policies (unlocked in Phase 3)
Block-level rules that act as global modifiers and that residents vote or argue about:
- **Rationing:** equal shares / by work done / by need (elderly, kids first).
- **Curfew & lights out** time.
- **Quarantine policy:** mandatory screening after expeditions? Mercy allowed?
- **Newcomer policy:** open gate / screened entry / closed gate.
- **Unit ownership:** private property respected or units collectivised?
- **Labour:** voluntary / rostered / "national service" for everyone over 16.

Every policy has supporters and opponents among the residents, so each one affects morale and trust differently by group.

---

## 11. Win / lose conditions

- **Lose:** everyone dead or turned. Or the **block falls** (void deck and stairs overrun to the top floor).
  Or **revolt** (trust at 0: the residents vote you out. You're the "block leader", not a dictator).
- **Score / soft win:** days survived, residents alive, babies born, kids educated, other blocks saved.
- **Endings (Phase 6):** each is a multi-step quest chain that you started by finding clues on
  earlier expeditions.

---

## 12. UI sketch (Fallout Shelter layout)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Day 23 • Afternoon • 🌧️ Thunderstorm • PSI 48 • 🔴 Grid: DOWN • 💧 Tank 62% │
│ 🍚 140  💧 310L  ⚡ 22  🩹 9  🔧 54   😊 61%   🤝 Trust 58   👥 34/38          │
├───────────────────────────────┬──────┬───────────────────────────────────┤
│ ROOFTOP  [Tank][Tank][Solar][Lookout]                                    │
├───────────────────────────────┼──────┼───────────────────────────────────┤
│ #12-101  Tan family (4)       │ LIFT │ #12-103 [Corridor Garden] 🌱      │
│ #11-101  [Sick Bay] 🩹 2/3    │ ║  ║ │ #11-103  Rahman family (5)        │
│ #10-101  [QUARANTINE] ⚠️ 1    │ ║▓▓║ │ #10-103  EMPTY — convert?         │
│  ...                          │STAIRS│  ...                              │
│ #02-101  [Workshop] 🔧        │ ▒▒▒▒ │ #02-103 [Storeroom] 📦            │
├───────────────────────────────┴──────┴───────────────────────────────────┤
│ VOID DECK  [Barricade ███░░] [Letterboxes] [Bicycle Bay] 🧟🧟 at gate!     │
└──────────────────────────────────────────────────────────────────────────┘
  [Outside Map]  [Residents]  [Policies]  [Radio]  [Event Log]
```

- **Drag residents** into units/jobs (Fallout Shelter style).
- **Tap a floor** to see the corridor: who's walking where, clutter, barricade state.
- **Event cards** pop up as dismissible prompts, and urgent ones pause time.

---

## 13. Tone & content notes

- Light, darkly comedic Singlish flavour (the uncles complaining, the WhatsApp forwards, "steady lah")
  balanced with real emotional beats (funerals, separated families).
- Every culture and community is a **source of strength**. Prejudice can appear as a **conflict for
  the player to resolve**, never as the game's own view.
- Avoid real brand names and logos in shipped art (say "the supermarket" or "the 24-hr supermarket"), and
  refer to government agencies generically or fictionalise them where needed.

---

## 14. Suggested first prototype scope (vertical slice)

1. Easy mode (8 storeys, 2 units/floor). Phase 0 + Phase 1 only.
2. 3 resources (food, water, morale) + infection.
3. Supermarket + park expeditions.
4. ~30 storylets, sunny/rain/haze weather.
5. Save/load and a day counter.

Then layer on power/water collapse (Phase 2) as the first "unlock".
