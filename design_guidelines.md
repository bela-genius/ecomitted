# Eccommitted Design Guidelines

## Design Approach
**Reference-Based + Educational Focus**: Drawing inspiration from modern environmental organizations (WWF, Greenpeace digital platforms) and educational platforms (Khan Academy, Duolingo) to create an engaging, youth-focused ecological experience that balances visual appeal with educational purpose.

## Core Design Principles
- **Optimistic Environmentalism**: Use vibrant, hopeful design language rather than alarmist tones
- **Student-Centered**: Youth-appropriate aesthetics with playful yet professional elements
- **Action-Oriented**: Every section should inspire engagement and participation
- **Accessible Learning**: Clear visual hierarchy that guides users through educational content

## Typography System

**Font Families**:
- Primary: Poppins (600 for headings, 500 for subheadings, 400 for body)
- Secondary: Montserrat (700 for impact statements, 600 for buttons)

**Scale**:
- Hero Headlines: text-5xl md:text-6xl lg:text-7xl (bold)
- Section Headers: text-3xl md:text-4xl lg:text-5xl
- Carousel Slides: text-2xl md:text-3xl lg:text-4xl
- Body Text: text-base md:text-lg
- Tips/Cards: text-lg
- Buttons: text-base md:text-lg (medium weight)

## Color Palette

**Primary Greens**:
- Vibrant Green: #2ecc71 (CTAs, accents, active states)
- Forest Green: #27ae60 (headers, hover states, dark mode accents)
- Sage Green: #a8e6cf (backgrounds, light mode soft fills)

**Supporting**:
- Sky Blue: #3498db (links, informational elements)
- Warm White: #f8fffe (light mode background)
- Charcoal: #1a1a1a (dark mode background)
- Soft Gray: #ecf0f1 (borders, dividers)

**Semantic**:
- Success/Growth: #2ecc71
- Information: #3498db
- Warning/Construction: #f39c12

## Layout System

**Spacing Primitives**: Use Tailwind units of 2, 4, 8, 12, 16, 20, 24 (p-2, gap-4, my-8, etc.)

**Container Strategy**:
- Max width: max-w-7xl for main content
- Section padding: py-16 md:py-20 lg:py-24
- Card padding: p-6 md:p-8
- Tight spacing: gap-2 or gap-4
- Medium spacing: gap-8 or gap-12
- Wide spacing: gap-16 or gap-20

**Grid Systems**:
- Tips Section: grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6
- Campaign Gallery: grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4
- Carousel: Full-width hero treatment with centered content

## Component Library

### Navigation
- Sticky header with transparent-to-solid transition on scroll
- Logo left, navigation center, theme toggle right
- Mobile: Hamburger menu with slide-in drawer
- Links with underline animation on hover (border-b-2 transition)

### Home Carousel
- Full-width hero section (min-h-[500px] md:min-h-[600px])
- 10 slides with smooth auto-transition (5-second intervals)
- Each slide: "¿Sabías que...?" format with large text + eco-icon
- Bottom text: "¡Únete al cambio!" in contrasting style
- Manual navigation: Arrow buttons (left/right) + dot indicators
- Semi-transparent overlay on background images for text readability
- Pause on hover for accessibility

### Institutional Block (Below Carousel)
- Centered content (max-w-4xl)
- Institutional quote in elegant serif or medium-weight sans
- "Empieza tu cambio 🌱" CTA button (large, green, rounded-full)

### Tips Cards
- Rounded cards (rounded-2xl) with soft shadow
- Icon at top (48px, green accent color)
- Title (text-xl, bold)
- Description (text-base, gray)
- Hover: Scale up slightly (scale-105), shadow intensifies, background shifts to sage green
- Border: 2px solid transparent → #2ecc71 on hover

### PRAE Construction Section
- Centered layout with construction icon/animation
- Playful animated gear or growing plant graphic
- "En Construcción" headline
- Teaser text about 5th Recycling Day
- Light background with dashed border pattern

### Campaign Gallery
- Masonry-style grid or uniform card grid
- Image cards with overlay text on hover
- Caption with action description
- "Quiero participar 💪" prominent CTA button
- Form modal: Simple fields (nombre, curso, idea) with green submit button

### About Section
- Two-column layout (md:grid-cols-2)
- Left: Institutional text with mission statement
- Right: Representative image of students in environmental activities
- Rounded image with subtle shadow

### Footer
- Dark background (#27ae60 or charcoal in dark mode)
- Three columns: Logo + tagline | Quick links | Social icons
- Copyright centered at bottom
- Social icons: Circular, hover scale effect

## Theme System

**Light Mode**:
- Background: #f8fffe
- Text: #1a1a1a
- Cards: white with soft shadows
- Accents: Vibrant green (#2ecc71)

**Dark Mode**:
- Background: #1a1a1a
- Text: #f8fffe
- Cards: #2a2a2a with green glow shadows
- Accents: Sage green (#a8e6cf)

**Toggle**: Moon/Sun icon in header, smooth transition (300ms) for all color changes

## Iconography
- Use Lucide React or Font Awesome for ecological icons
- Icon set: Leaf, Recycle, Droplet, Lightbulb, TreeDeciduous, Bike, Heart, Users, Sprout
- Consistent 24px or 32px size for list items
- 48px for feature cards
- 64px for section headers

## Animations (Subtle & Purposeful)
- Carousel transitions: Fade + slide (400ms ease-in-out)
- Card hover: Scale + shadow (200ms)
- Page section entrance: Fade-up on scroll (stagger children by 100ms)
- Button hover: Slight scale (1.05) + shadow enhancement
- Theme toggle: Color transition (300ms) + icon rotation (180deg)
- NO distracting parallax or continuous animations

## Images

**Hero Carousel Backgrounds**:
- 10 high-quality images of nature, students in eco-activities, recycling, plants, solar panels, etc.
- Optimized for web (WebP format preferred)
- Aspect ratio: 16:9 or 21:9 for wide displays
- Overlay: Semi-transparent dark gradient (bottom-to-top) for text readability

**About Section Image**:
- Students engaged in environmental activities (planting, recycling, outdoor learning)
- Horizontal orientation, warm natural lighting
- Place on right side of two-column layout

**Campaign Gallery Images**:
- Real photos from school events (if available) or representative eco-action images
- Uniform aspect ratio (4:3 or 1:1 for cards)
- Include: Tree planting, recycling stations, environmental fairs, student groups

**No large standalone hero image outside carousel** - carousel serves as the hero element

## Responsive Behavior
- Mobile: Single column, stacked navigation, carousel at reduced height
- Tablet: Two-column grids, expanded navigation
- Desktop: Full multi-column layouts, larger text scales
- Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)

## Accessibility
- High contrast text (WCAG AA minimum)
- Focus states: 2px green outline for keyboard navigation
- Alt text for all images
- Semantic HTML5 structure
- Carousel pause button
- Form labels clearly associated with inputs