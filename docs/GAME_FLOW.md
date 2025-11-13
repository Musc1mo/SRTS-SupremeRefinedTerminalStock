# GAME FLOW & CINEMATICS

> **Design Document for SRTS: Supreme Refined Terminal Stock**  
> *Player Journey from Main Menu to Gameplay*

---

## 🎬 INTRO SEQUENCE

### Opening Cinematic (Pre-Menu)

**Visual Style:** Documentary horror aesthetic, grainy film quality

**Script:**
```
[Black screen. Geiger counter ticking sounds]

NARRATOR (distorted, echoing):
"On November 7th, 2025, humanity ceased to exist."

[Flickering footage: empty streets, abandoned cars, fallen phones]

"Radiation. Bioweapons. The details no longer matter.
What matters is what they left behind."

[Camera slowly pans across a kitchen counter, past wilted plants, 
stopped clocks, an open refrigerator door with condensation]

"On stoves. In refrigerators. Across the planet.
Millions of soups remained."

[Extreme close-up: surface of soup beginning to bubble]

"The last meals of a dead civilization..."

[Microscopic view: cells dividing, evolving rapidly]

"...became the first meals of the next."

[Title card fades in with eldritch text]
S̴̰͊ ̶̹̈O̴̧͝ ̵̰̕U̷͎̒ ̶̰̈P̴̰̾

"From ashes to soup, from soup to meat, from there to S̴̰͊ ̶̹̈O̴̧͝ ̵̰̕U̷͎̒ ̶̰̈P̴̰̾"
"Humanity failed its Complementation. We will succeed."

[Fade to main menu]
```

**Audio:**
- Ambient: Wind, distant sirens fading out, Geiger counter
- Music: Minimalist drone, building to distorted orchestral crescendo
- SFX: Bubbling liquid, microscopic clicking sounds

---

## 🗺️ CIVILIZATION SELECTION FLOW

### 1. Main Menu → New Game

Player clicks **"NEW GAME"** button.

---

### 2. World Map Screen

**Visual Design:**

- **Camera Angle:** Orbital view, as if from the ISS
- **Color Palette:** Desaturated grays, muted blues/greens
- **Lighting:** No city lights. No signs of electricity. Eternal twilight.
- **Details:**
  - Cloud cover moves slowly
  - No airplane contrails
  - Continents are visible but lifeless
  - Occasional lightning flashes illuminate empty metropolises

**UI Overlay:**

```
╔═══════════════════════════════════════════════════════════╗
║                  SELECT YOUR CIVILIZATION                  ║
║                                                            ║
║  [MACRO-REGIONS highlighted on map]                        ║
║                                                            ║
║  ASIA  •  EUROPE  •  AFRICA  •  AMERICAS  •  MIDDLE EAST  ║
╚═══════════════════════════════════════════════════════════╝
```

**Interaction:**

1. Player hovers over a **macro-region** (e.g., ASIA)
2. Region **pulses with soft glow**
3. **Soup icons appear** as pinpoints within that region:
   - 🍜 Miso (Tokyo)
   - 🍜 Ramen (Osaka)
   - 🍲 Pho (Hanoi)
   - 🍲 Tom Yam (Bangkok)
   - 🍜 Laksa (Singapore)

4. Player clicks on **specific soup icon** (e.g., Tom Yam in Bangkok)

---

### 3. Location Flyover Cinematic

**[AUTOMATICALLY TRIGGERED AFTER SOUP SELECTION]**

#### Example: Tom Yam (Bangkok, Thailand)

**Shot 1: Descent from Orbit (5 seconds)**
- Camera descends rapidly through clouds
- Bangkok skyline comes into view
- No lights. Overgrown vegetation on skyscrapers.

**Shot 2: Street-Level Flyover (8 seconds)**
- Camera glides through **stereotypical Bangkok streets**:
  - Tuk-tuks abandoned mid-street
  - Faded Thai script on shop signs
  - Wilted lotus flowers in street vendor carts
  - Buddhist shrine with incense long burned out
  - Monsoon rain dripping from corrugated metal roofs

**Shot 3: Entering Building (4 seconds)**
- Camera approaches a **typical Bangkok apartment building**
  - Peeling yellow paint
  - Clothes still hanging on balcony lines (tattered, weathered)
  - Open window with curtains blowing in wind

**Shot 4: Interior Apartment (6 seconds)**
- Camera glides through narrow hallway
- Past family photos on wall (faces blurred, time-worn)
- Buddhist altar with wilted flowers
- Kitchen visible ahead

**Shot 5: The Refrigerator (4 seconds)**
- Camera stops in front of **old, slightly rusty refrigerator**
- Door is ajar, light flickering faintly (last gasp of battery backup)
- Camera **pushes through the door**

**Shot 6: Inside the Fridge (3 seconds)**
- Camera focuses on a **clay pot of Tom Yam soup**
- Surface is bubbling slightly
- Extreme close-up: microscopic life visible

**Shot 7: Transition to Gameplay (2 seconds)**
- Camera **dives into the soup**
- Liquid envelops screen
- Fade to cellular view → **GAMEPLAY BEGINS**

---

## 🎮 TRANSITION TO GAMEPLAY

**Visual:**
- Screen "liquifies" — soup texture fills viewport
- Zoom into microscopic scale
- First cell spawns in center of screen

**UI Elements Appear:**
```
╔═══════════════════════════════════════════════╗
║  TOM YAM CIVILIZATION                         ║
║  Location: Bangkok, Thailand                  ║
║                                               ║
║  Stage 1: CELLULAR SURVIVAL                   ║
║                                               ║
║  [Resource Counter]  [Cell Count]  [Time]     ║
╚═══════════════════════════════════════════════╝
```

**Gameplay starts immediately.**

---

## 📋 LOCATION-SPECIFIC CINEMATICS (All Soups)

### Visual Stereotypes for Each Civilization

**ASIA**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Miso** | Tokyo, Japan | Neon signs (dark), vending machines, sakura petals, small apartment, modern fridge |
| **Ramen** | Osaka, Japan | Ramen shop storefront, red lanterns (unlit), kitchen pots, industrial fridge |
| **Pho** | Hanoi, Vietnam | Motorbike chaos (frozen), street vendors, narrow alley, metal pot on stove |
| **Tom Yam** | Bangkok, Thailand | Tuk-tuks, Buddhist shrines, monsoon rain, clay pot in old fridge |
| **Laksa** | Singapore | High-rise HDB flat, hawker center stalls, modern kitchen, tupperware in fridge |

**EUROPE**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Borscht** | Kyiv, Ukraine | Soviet-era apartment blocks, Orthodox church domes, babushka's kitchen, enamel pot |
| **French Onion** | Paris, France | Cobblestone streets, café tables (empty), Eiffel Tower (distant), ceramic crock |
| **Bouillabaisse** | Marseille, France | Mediterranean harbor, fishing boats, stone cottage, cast iron pot |
| **Gazpacho** | Seville, Spain | Flamenco posters, tiled courtyards, siesta shutters, glass pitcher |
| **Caldo Verde** | Lisbon, Portugal | Tram tracks, azulejo tiles, hillside homes, earthenware bowl |
| **Avgolemono** | Athens, Greece | White-blue architecture, olive trees, ancient ruins (distant), ceramic tureen |

**AFRICA**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Egusi** | Lagos, Nigeria | Colorful markets, corrugated roofs, vibrant textiles, clay pot on charcoal stove |
| **Peanut Soup** | Addis Ababa, Ethiopia | Coffee ceremony setup, injera basket, highland landscape, clay jar |

**LATIN AMERICA**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Chupe de Mariscos** | Lima, Peru | Coastal cliffs, fishing nets, colonial architecture, copper pot |
| **Tacacá** | Belém, Brazil | Amazon river, colorful houses on stilts, indigenous art, gourd bowl |
| **Canja de Galinha** | São Paulo, Brazil | Favela hillsides, graffiti art, football murals, grandmother's kitchen |
| **Fanesca** | Quito, Ecuador | Andean mountains, church bells (silent), market textiles, ceremonial bowl |

**MIDDLE EAST**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Ash-e Reshteh** | Tehran, Iran | Persian carpets, calligraphy, courtyard fountain, ornate serving dish |
| **Shorba** | Cairo, Egypt | Minarets, Nile view, spice bazaar, brass pot |

**NORTH AMERICA**

| Soup | Location | Stereotypical Imagery |
|------|----------|----------------------|
| **Jewish Chicken Soup** | New York, USA | Brooklyn brownstones, deli signs, fire escapes, stockpot in cramped kitchen |

---

## 🎨 CINEMATIC PRODUCTION NOTES

### Technical Specs

**Camera:**
- Unreal Engine 5 / Unity cinematic camera
- FOV: 60-75° (cinematic)
- Motion: Smooth bezier curves, no abrupt movements

**Post-Processing:**
- Slight chromatic aberration (abandoned world feel)
- Vignetting on edges
- Film grain overlay (16mm documentary aesthetic)
- Color grading: Desaturated, cool tones

**Audio Design:**
- **Ambient layers:**
  - Wind
  - Distant thunder
  - Creaking buildings
  - Dripping water
- **Cultural audio cues:**
  - Faint echoes of traditional music (distorted, like a memory)
  - Wind chimes, prayer bells (for religious locations)
- **Transition sound:**
  - Deep subwoofer "descent" tone as camera enters fridge
  - Liquid "splash" as gameplay begins

### Animation Timeline

```
Total Cinematic Length: ~30-35 seconds per soup

00:00 - 00:05  |  Orbital descent
00:05 - 00:13  |  Street flyover
00:13 - 00:17  |  Building entry
00:17 - 00:23  |  Interior navigation
00:23 - 00:27  |  Refrigerator focus
00:27 - 00:30  |  Soup close-up
00:30 - 00:32  |  Liquid transition
00:32          |  GAMEPLAY START
```

---

## ✅ DESIGN GOALS SUMMARY

1. **Emotional Impact:** Player feels the weight of humanity's extinction
2. **Cultural Authenticity:** Each location feels distinct and recognizable
3. **Atmosphere:** Post-apocalyptic beauty, not generic zombie wasteland
4. **Immersion:** Seamless transition from cinematic to gameplay
5. **Replayability:** Each soup selection offers unique visual journey

---

## 📝 IMPLEMENTATION CHECKLIST

- [ ] Create 3D world map with macro-regions
- [ ] Design UI for soup selection (icons, tooltips)
- [ ] Model 20+ location-specific environments (low-poly for cinematics)
- [ ] Animate camera paths for each soup's flyover
- [ ] Record/compose location-specific ambient audio
- [ ] Create liquid "splash" transition effect
- [ ] Implement skip button (ESC key) for returning players
- [ ] Add subtitles/localization support for narrator

---

**End of Game Flow Document**
