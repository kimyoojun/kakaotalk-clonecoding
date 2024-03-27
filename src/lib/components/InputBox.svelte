<script lang="ts">
  export let inputName = ""
  export let value = ""
</script>

<input class="input-box" placeholder={inputName} bind:value={value}/>

<style>
  .input-box {
    width: 252px;
    height: 36px;
    border: 0.5px solid rgb(202, 202, 202);
    outline: none;
    padding: 0 10px;
  }
</style>