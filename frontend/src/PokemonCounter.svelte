<script>
  // Svelte 5 runes syntax
  let { pokemonData = [] } = $props();

  let selectedType = $state('');
  let searchQuery = $state('');

  // Derived state using $derived
  let filteredPokemon = $derived(() => {
    let filtered = pokemonData;

    if (selectedType) {
      filtered = filtered.filter(p =>
        p.types && p.types.toLowerCase().includes(selectedType.toLowerCase())
      );
    }

    if (searchQuery) {
      filtered = filtered.filter(p =>
        p.name.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    return filtered;
  });

  let count = $derived(filteredPokemon().length);

  // Get unique types
  let allTypes = $derived(() => {
    const types = new Set();
    pokemonData.forEach(p => {
      if (p.types) {
        p.types.split(',').forEach(t => types.add(t.trim()));
      }
    });
    return Array.from(types).sort();
  });
</script>

<div class="pokemon-counter">
  <div class="counter-header">
    <h3>Interactive Pokemon Counter</h3>
    <div class="count-badge">{count} Pokemon</div>
  </div>

  <div class="filters">
    <div class="filter-group">
      <label for="svelte-search">Quick Search:</label>
      <input
        id="svelte-search"
        type="text"
        bind:value={searchQuery}
        placeholder="Type to search..."
      />
    </div>

    <div class="filter-group">
      <label for="svelte-type">Filter by Type:</label>
      <select id="svelte-type" bind:value={selectedType}>
        <option value="">All Types</option>
        {#each allTypes() as type}
          <option value={type}>{type}</option>
        {/each}
      </select>
    </div>
  </div>

  {#if searchQuery || selectedType}
    <div class="active-filters">
      <strong>Active Filters:</strong>
      {#if searchQuery}
        <span class="filter-tag">Search: "{searchQuery}"</span>
      {/if}
      {#if selectedType}
        <span class="filter-tag type-{selectedType}">{selectedType}</span>
      {/if}
      <button
        class="clear-btn"
        onclick={() => {
          searchQuery = '';
          selectedType = '';
        }}
      >
        Clear All
      </button>
    </div>
  {/if}
</div>

<style>
  .pokemon-counter {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  }

  .counter-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .counter-header h3 {
    margin: 0;
    font-size: 1.5em;
  }

  .count-badge {
    background: rgba(255, 255, 255, 0.2);
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 1.2em;
    font-weight: bold;
    backdrop-filter: blur(10px);
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }

  .filters {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
  }

  .filter-group {
    display: flex;
    flex-direction: column;
  }

  .filter-group label {
    margin-bottom: 8px;
    font-weight: bold;
    font-size: 0.9em;
  }

  .filter-group input,
  .filter-group select {
    padding: 12px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 8px;
    font-size: 1em;
    background: rgba(255, 255, 255, 0.9);
    transition: all 0.3s;
  }

  .filter-group input:focus,
  .filter-group select:focus {
    outline: none;
    border-color: white;
    background: white;
    box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.3);
  }

  .active-filters {
    margin-top: 15px;
    padding: 15px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .filter-tag {
    background: rgba(255, 255, 255, 0.3);
    padding: 5px 12px;
    border-radius: 15px;
    font-size: 0.9em;
    backdrop-filter: blur(5px);
  }

  .clear-btn {
    margin-left: auto;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid white;
    color: white;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
  }

  .clear-btn:hover {
    background: white;
    color: #667eea;
    transform: translateY(-2px);
  }

  @media (max-width: 768px) {
    .filters {
      grid-template-columns: 1fr;
    }

    .counter-header {
      flex-direction: column;
      gap: 15px;
    }
  }
</style>
