"""Restaurant data management module with comprehensive Geediga Dahabka Restaurant information"""
import os

# Comprehensive Geediga Dahabka Restaurant Data
COMPREHENSIVE_RESTAURANT_DATA = """
# Geediga Dahabka Restaurant – Full Profile

## 🏢 Restaurant Overview

**Name:** Geediga Dahabka Restaurant  
**Established:** 2015  
**Type:** Family & Business Dining  
**Owner:** Fartun Mohamed  
**Manager:** Abdiqani Yusuf
**Seating Capacity:** 120 indoor, 50 outdoor
**Average Check:** $25-30 per person
**Reservation Policy:** Recommended for groups of 6+ people

**Description:**  
Geediga Dahabka Restaurant is a premium Somali restaurant located in the heart of Mogadishu, Somalia. Founded by local entrepreneur Fartun Mohamed, it has become one of the most celebrated culinary destinations in East Africa. The restaurant offers a unique blend of traditional Somali flavors with modern dining elegance. It was established to provide a place where both locals and international guests can experience authentic Somali culture through food, hospitality, and ambiance.

## 📜 History & Milestones

- **2015:** Restaurant founded by Fartun Mohamed
- **2016:** Won "Best New Restaurant" at Mogadishu Food Festival
- **2017:** Expanded to include outdoor seating area
- **2018:** Launched catering services
- **2019:** Featured in "Top 10 Restaurants in East Africa" by African Food Network
- **2020:** Implemented online ordering system
- **2021:** Opened private VIP rooms
- **2022:** Celebrated 7th anniversary with special menu
- **2023:** Launched cooking classes and culinary workshops

## 📍 Location

**Address:** Maka Al-Mukarama Road, Hodan District, Mogadishu, Somalia  
**Coordinates:** Latitude 2.0416, Longitude 45.3425
**Parking:** Free valet parking available
**Accessibility:** Wheelchair accessible, elevator available

**Contact Info:**
- Phone: +252 61 555 7890
- Email: info@geedigdahabka.so
- Website: www.geedigdahabka.so
- Social Media: @geedigdahabka (Instagram, Facebook, Twitter)
- **For food orders: +252 61 1499124**

## 🏬 Branches & Locations

| Branch Name        | Address                                        | Contact          | Seating Capacity       | Special Features                    |
| ------------------ | ---------------------------------------------- | ---------------- | ---------------------- | ----------------------------------- |
| **Main Branch**    | Maka Al-Mukarama Road, Hodan District          | +252 61 555 7890 | 120 Indoor, 50 Outdoor | VIP rooms, live cooking, valet      |
| **KM4 Branch**     | KM4 Area, Near Peace Tower                     | +252 61 555 7891 | 80 Indoor              | Drive-thru, business lunch specials |
| **Airport Branch** | Aden Adde International Airport Arrival Lounge | +252 61 555 7892 | 40 Indoor              | Quick meals, tourist specials       |
| **Banadir Branch** | Banadir Hospital Complex, near cafeteria area  | +252 61 555 7893 | 60 Indoor              | Hospital staff discount, takeaway   |

> All branches offer dine-in, takeaway, and delivery services within a 5km radius.

## 🕰️ Opening Hours

| Day       | Hours               | Special Notes                   |
| --------- | ------------------- | ------------------------------- |
| Monday    | 10:00 AM – 10:00 PM | Business lunch specials 12-2 PM |
| Tuesday   | 10:00 AM – 10:00 PM | Live music 7-9 PM               |
| Wednesday | 10:00 AM – 10:00 PM | Family night discounts          |
| Thursday  | 10:00 AM – 11:00 PM | Ladies night specials           |
| Friday    | 1:30 PM – 11:00 PM  | Special Jummah menu             |
| Saturday  | 10:00 AM – 11:30 PM | Weekend brunch 10 AM - 2 PM     |
| Sunday    | 10:00 AM – 9:00 PM  | Early bird specials 5-7 PM      |

## 🍽️ Services

- Dine-in with traditional Somali decor and seating
- Home delivery within Mogadishu (5km radius)
- Takeaway and drive-thru service
- Event catering (weddings, aqal gal, corporate)
- Private VIP rooms (capacity: 20-30 people)
- Online reservations
- Live cooking stations
- Cooking classes (Saturdays 2-4 PM)
- Corporate event hosting
- Wedding planning services
- Food photography sessions
- Chef's table experience (by reservation)

## 👨‍🍳 Staff

- **Head Chef:** Xasan Cali – 20+ years experience, expert in Somali & Arabic cuisine
- **Menu Advisor:** Layla Omar – Nutritionist & culinary consultant
- **Chefs:** 6
- **Service Staff:** 8
- **Support Staff:** 5
- **Cleaning Staff:** 3
- **Security:** 2
- **Event Coordinators:** 2
- **Delivery Drivers:** 4
- **Marketing Team:** 2

## 🍽️ Complete Menu

### 🥟 Starters

- **Sambuus** – $1.50  
  _Fried pastries filled with spiced minced beef or vegetables._

- **Chicken Soup** – $2.50  
  _Somali-style chicken soup with carrots and spices._

- **Maraq Qudaar** – $2.00  
  _Hearty vegetable soup with Somali herbs._

- **Grilled Kalluun** – $3.00  
  _Marinated grilled fish served with lime._

- **Laxoox Bites** – $2.50  
  _Mini Somali sourdough pancakes with pepper sauce._

### 🍔 Fast Food

- **Chicken Burger** – $5.00  
  _Crispy chicken burger with fresh vegetables._

- **Meat Burger** – $5.00  
  _Beef burger with traditional spices._

- **Philadelphia Chicken** – $5.50
  _Chicken Philadelphia sandwich with cheese._

- **Philadelphia Meat** – $5.50
  _Meat Philadelphia sandwich with cheese._

- **Philadelphia Meat Sandwich** – $5.00
  _Traditional meat sandwich Philadelphia style._

- **French Fries** – $2.00
  _Crispy golden French fries._

- **Crispy Chicken** – $5.00
  _Crispy fried chicken pieces._

- **Chicken Nuggets** – $5.00
  _Tender chicken nuggets._

- **Double Chicken Burger** – $7.50
  _Double chicken patty burger._

### 🍛 Main Courses

- **Bariis Iskukaris** – $6.50  
  _Spiced rice with raisins, served with goat meat._

- **Suqaar Digaag** – $5.50  
  _Chicken suqaar with onions, peppers, and sabaayad._

- **Baasto Somali** – $6.00  
  _Spaghetti with spicy Somali-style beef sauce._

- **Muufo iyo Hilib** – $6.00  
  _Corn flatbread served with lamb stew._

- **Kaluun Duban** – $7.00  
  _Whole grilled fish with cumin and garlic._

- **Odkac iyo Rooti** – $7.50  
  _Sun-dried camel meat with Somali flatbread._

- **Hilib Ari Duban** – $7.00  
  _Roasted goat meat served with rice and dates._

- **Digaag Duban** – $6.50  
  _Roasted chicken with canjeero and yogurt sauce._

- **Camel Meat Steak** – $8.00  
  _Grilled camel steak with date chutney._

### 🌿 Vegetarian Options

- **Qudaar Kari** – $4.00  
  _Vegetable stew in coconut tomato sauce._

- **Canjeero Combo** – $4.50  
  _Canjeero served with lentils and chutney._

- **Baradhada Qudaar** – $4.00  
  _Stir-fried potatoes with Somali spices._

- **Muufo iyo Qudaar** – $4.50  
  _Flatbread with vegetable stew._

### 🍰 Desserts

- **Halwo** – $2.00  
  _Somali sweet made with cornstarch and ghee._

- **Basbousa** – $2.50  
  _Semolina cake with syrup and coconut._

- **Canjeero Malab** – $2.50  
  _Canjeero pancakes with honey and dates._

- **Maqmaaq** – $2.00  
  _Sesame biscuits with Somali tea._

- **Doolshe Somali** – $2.50  
  _Cardamom-flavored Somali cake._

- **Gashaato** – $2.00  
  _Coconut balls with sugar and cardamom._

- **Kac Kac** – $1.50  
  _Crispy fried Somali cookies._

- **Malab Macaan** – $2.50  
  _Honey custard with saffron._

### 🥤 Beverages

- **Shaah Somali** – $1.00  
  _Spiced tea with cinnamon and cardamom._

- **Qaxwo Carbeed** – $1.50  
  _Arabic coffee with cardamom._

- **Ayr** – $1.50  
  _Traditional Somali yogurt drink._

- **Fresh Mango Juice** – $2.00  
  _Freshly squeezed mango juice._

- **Camel Milk Smoothie** – $3.00  
  _Camel milk shake with dates._

- **Tamarind Juice** – $2.00  
  _Sweet and tangy tamarind drink._

- **Minted Ayr** – $2.00  
  _Yogurt drink with mint._

- **Lemon Ginger Cooler** – $2.00  
  _Lemonade with ginger and honey._

### 🥤 Shakes

- **Chocolate Shake** – $2.00  
  _Rich, creamy chocolate blended with milk and ice cream._

- **Strawberry Shake** – $3.00  
  _Fresh strawberries blended with milk and vanilla ice cream._

- **Banana Shake** – $1.50  
  _Ripe bananas pureed into a smooth, milky delight._

- **Vanilla Shake** – $2.00  
  _Classic vanilla flavor made with real ice cream and milk._

- **Mango Shake** – $2.00  
  _Sweet mango chunks blended into a tropical, refreshing shake._

### 🧊 Iced Beverages

- **Iced Macchiato** – $3.00  
  _Chilled espresso layered with creamy milk and ice._

- **Iced Latte** – $3.00  
  _Smooth espresso mixed with cold milk and served over ice._

- **Iced Cappuccino** – $3.00  
  _A bold espresso base with cold frothy milk and ice._

- **Lemon Iced Tea** – $1.50  
  _Freshly brewed tea infused with zesty lemon and served cold._

- **Strawberry Iced Tea** – $2.50  
  _Sweetened tea with fresh strawberry flavor over ice._

- **Mango Iced Tea** – $2.50  
  _Iced tea blended with juicy mango for a tropical twist._

- **Iced Americano** – $2.50  
  _Espresso diluted with cold water and poured over ice._

## 💰 Special Offers & Promotions

### Weekly Specials

- **Monday:** 20% off on all rice dishes
- **Tuesday:** Buy 1 Get 1 Free on selected appetizers
- **Wednesday:** Family package discount (15% off for 4+ people)
- **Thursday:** Ladies night - 25% off on desserts
- **Friday:** Special Jummah menu with 10% discount
- **Saturday:** Weekend brunch special (10 AM - 2 PM)
- **Sunday:** Early bird special (5-7 PM)

### Monthly Promotions

- **First Week:** Student discount (15% off with valid ID)
- **Second Week:** Senior citizen special (20% off)
- **Third Week:** Corporate lunch deals
- **Fourth Week:** Birthday month celebration (free dessert)

### Loyalty Program

- Points system: 1 point per $1 spent
- 100 points = $10 discount
- Birthday rewards
- Special member-only events
- Priority reservation

## ⭐ Customer Reviews & Ratings

**Overall Rating:** 4.8/5 (Based on 1,200+ reviews)

**Top Reviews:**
1. "Best Somali restaurant in Mogadishu! The Bariis Iskukaris is to die for." - Ahmed K. (5/5)
2. "Amazing atmosphere and authentic flavors. Their camel meat dishes are exceptional." - Fatima M. (5/5)
3. "Great service and beautiful traditional decor. Perfect for family gatherings." - Omar S. (4.5/5)

## 🌟 Awards & Recognition

- Best Restaurant in Mogadishu (2019-2023)
- Excellence in Somali Cuisine (2022)
- Top 10 East African Restaurants (2021)
- Best Business Lunch (2020)
- Customer Service Excellence (2019)

## 🚚 Delivery Information

**Delivery Zones:**
- Zone 1 (0-2km): 15-20 minutes, Free delivery for orders above $30
- Zone 2 (2-4km): 25-35 minutes, $2 delivery fee
- Zone 3 (4-5km): 35-45 minutes, $3 delivery fee
- Minimum order: $15

**Delivery Hours:**
- Weekdays: 11:00 AM - 9:30 PM
- Weekends: 11:00 AM - 10:00 PM

## 🎉 Special Events & Programs

**Regular Events:**
- Traditional Music Night (Every Tuesday)
- Cooking Masterclass (First Saturday monthly)
- Family Day (Last Sunday monthly)
- Business Lunch Special (Weekdays 12-2 PM)
- Ladies Night (Every Thursday)

**Annual Events:**
- Ramadan Iftar Special Menu
- Eid Celebrations
- Independence Day Feast
- Anniversary Celebration
- New Year's Eve Gala

## ❓ Frequently Asked Questions

### Reservations
**Q: How far in advance should I make a reservation?**
A: For regular dining, 24 hours is recommended. For groups of 8+ or special occasions, 1 week in advance.

### Menu & Dietary Requirements
**Q: Do you offer vegetarian options?**
A: Yes, we have a dedicated vegetarian menu section.

**Q: Is the menu halal?**
A: Yes, all our meat is 100% halal certified.

### Payment & Pricing
**Q: What payment methods do you accept?**
A: Cash, credit cards, mobile payments, and major digital wallets.

### Events & Catering
**Q: What is the minimum order for catering?**
A: Minimum 20 people for off-site catering.

**Q: Can you host private events?**
A: Yes, we have private rooms for 20-30 people.

## 📱 Digital Presence

**Social Media:**
- Instagram: @geedigdahabka (50K followers)
- Facebook: Geediga Dahabka (30K likes)
- Twitter: @geedigdahabka (20K followers)
- TikTok: @geedigdahabka (100K followers)

**Contact for Orders:** +252 61 1499124
"""

def load_restaurant_info():
    """Load restaurant information - now returns the comprehensive data directly"""
    return COMPREHENSIVE_RESTAURANT_DATA

def extract_menu_items(content):
    """Extract menu items from the comprehensive content"""
    menu_items = []
    menu_section = False
    current_category = None
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Check for menu section start
        if '## 🍽️ Complete Menu' in line or '## 🍽️ Menu' in line or '## Menu' in line:
            menu_section = True
            continue
            
        # Check for category headers
        if menu_section and line.startswith('###'):
            current_category = line.replace('###', '').strip()
            # Remove emoji and clean up category name
            current_category = current_category.replace('🥟', '').replace('🍔', '').replace('🍛', '').replace('🌿', '').replace('🍰', '').replace('🥤', '').replace('🧊', '').strip()
            continue
            
        # Check for menu items
        if menu_section and line.startswith('- **') and '–' in line:
            try:
                # Parse: - **Item Name** – $Price _Description_
                item_line = line.replace('- **', '')
                
                if '**' in item_line and '–' in item_line:
                    name_part = item_line.split('**')[0].strip()
                    rest_part = item_line.split('**')[1].strip()
                    
                    if rest_part.startswith('–'):
                        price_desc = rest_part[1:].strip()
                        price = price_desc.split()[0].replace('$', '').strip()
                        
                        # Extract description between underscores
                        description = ''
                        if '_' in price_desc:
                            desc_parts = price_desc.split('_')
                            if len(desc_parts) >= 2:
                                description = desc_parts[1].strip()
                        
                        menu_items.append({
                            'category': current_category,
                            'name': name_part,
                            'price': f"${price}",
                            'description': description
                        })
                        
            except Exception as e:
                print(f"Error parsing menu item: {line} - {e}")
                continue
                
        # Check for end of menu section
        elif menu_section and line.startswith('##') and '🍽️' not in line and 'Menu' not in line:
            break
            
    return menu_items

def extract_hours(content):
    """Extract opening hours from the comprehensive content"""
    hours = {}
    hours_section = False
    
    for line in content.split('\n'):
        if '## 🕰️ Opening Hours' in line or '## Opening Hours' in line:
            hours_section = True
            continue
            
        if hours_section and '|' in line and len(line.split('|')) >= 4:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 4 and parts[1] and 'Day' not in parts[1] and parts[1]:
                day = parts[1]
                time = parts[2] if len(parts) > 2 else ''
                notes = parts[3] if len(parts) > 3 else ''
                hours[day] = {'time': time, 'notes': notes}
                
        elif hours_section and line.startswith('##') and '🕰️' not in line and 'Opening Hours' not in line:
            break
            
    return hours

def extract_branches(content):
    """Extract branch information from the comprehensive content"""
    branches = {}
    branch_section = False
    
    for line in content.split('\n'):
        if '## 🏬 Branches & Locations' in line or '## Branches' in line:
            branch_section = True
            continue
            
        if branch_section and '|' in line and len(line.split('|')) >= 6:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6 and '**' in parts[1]:
                name = parts[1].replace('**', '')
                address = parts[2] if len(parts) > 2 else ''
                contact = parts[3] if len(parts) > 3 else ''
                capacity = parts[4] if len(parts) > 4 else ''
                features = parts[5] if len(parts) > 5 else ''
                branches[name] = {
                    'address': address,
                    'contact': contact,
                    'capacity': capacity,
                    'features': features
                }
                
        elif branch_section and line.startswith('##') and '🏬' not in line and 'Branches' not in line:
            break
            
    return branches

def extract_services(content):
    """Extract services information"""
    services = []
    services_section = False
    
    for line in content.split('\n'):
        if '## 🍽️ Services' in line or '## Services' in line:
            services_section = True
            continue
            
        if services_section and line.startswith('- '):
            service = line.replace('- ', '').strip()
            services.append(service)
            
        elif services_section and line.startswith('##') and '🍽️' not in line and 'Services' not in line:
            break
            
    return services

def extract_special_offers(content):
    """Extract special offers and promotions"""
    offers = {}
    offers_section = False
    current_subsection = None
    
    for line in content.split('\n'):
        if '## 💰 Special Offers & Promotions' in line:
            offers_section = True
            continue
            
        if offers_section and line.startswith('###'):
            current_subsection = line.replace('###', '').strip()
            offers[current_subsection] = []
            continue
            
        if offers_section and current_subsection and line.startswith('- **'):
            offer = line.replace('- **', '').replace('**', '').strip()
            offers[current_subsection].append(offer)
            
        elif offers_section and line.startswith('##') and '💰' not in line:
            break
            
    return offers

# Load and process restaurant data
print("Loading comprehensive restaurant data...")
RESTAURANT_INFO = load_restaurant_info()
MENU_ITEMS = extract_menu_items(RESTAURANT_INFO)
OPENING_HOURS = extract_hours(RESTAURANT_INFO)
BRANCHES = extract_branches(RESTAURANT_INFO)
SERVICES = extract_services(RESTAURANT_INFO)
SPECIAL_OFFERS = extract_special_offers(RESTAURANT_INFO)

print(f"✅ Loaded {len(MENU_ITEMS)} menu items")
print(f"✅ Loaded {len(OPENING_HOURS)} opening hours")
print(f"✅ Loaded {len(BRANCHES)} branches")
print(f"✅ Loaded {len(SERVICES)} services")
print(f"✅ Loaded special offers: {list(SPECIAL_OFFERS.keys())}")

# Display sample menu items by category
menu_by_category = {}
for item in MENU_ITEMS:
    category = item['category']
    if category not in menu_by_category:
        menu_by_category[category] = []
    menu_by_category[category].append(item)

print(f"✅ Menu categories: {list(menu_by_category.keys())}")
