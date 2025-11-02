import { mount } from 'svelte';
import PokemonCounter from './PokemonCounter.svelte';

// Export a function to mount the component
// This will be called from the Django template
window.mountPokemonCounter = function(target, props) {
  return mount(PokemonCounter, {
    target: target,
    props: props
  });
};
