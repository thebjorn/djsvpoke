# Svelte 5 + Django Integration

This directory contains Svelte 5 components that are integrated into the Django Pokedex app.

## Setup

The project uses Vite to build Svelte 5 components and outputs them to Django's static files directory.

## Development

```bash
cd frontend
npm run dev
```

This starts the Vite dev server for rapid component development.

## Building for Production

```bash
cd frontend
npm run build
```

This builds the Svelte components and outputs them to `pokemon/static/svelte/`:
- `pokemon-component.js` - The compiled JavaScript
- `pokemon-component.css` - The component styles

## How It Works

1. **Svelte Component** (`src/PokemonCounter.svelte`): A Svelte 5 component using the new runes API ($state, $derived, $props)
2. **Entry Point** (`src/main.js`): Exports a `mountPokemonCounter` function to the global window object
3. **Vite Config** (`vite.config.js`): Configured to output to Django's static directory
4. **Django Template**: Loads the built JS/CSS and mounts the component with Pokemon data

## Creating New Components

1. Create a new `.svelte` file in `src/`
2. Import and mount it in `src/main.js`
3. Run `npm run build`
4. Include it in your Django template

## Example Component Usage

The `PokemonCounter` component demonstrates:
- Svelte 5 runes syntax ($state, $derived, $props)
- Real-time filtering and search
- Props passed from Django template
- Styled with scoped CSS
