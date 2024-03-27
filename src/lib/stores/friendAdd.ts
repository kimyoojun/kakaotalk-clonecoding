import { writable } from 'svelte/store'

export interface ToggleStore {
  friendAdd: boolean
}

export const isToggleStore = writable<ToggleStore>({
  friendAdd: false,
})
