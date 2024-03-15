<script>
  export let btnName = ""
  export let onClick

  const handleClick = () => {
    onClick()
  }
</script>

<button class="btn-box" on:click={handleClick}>{btnName}</button>

<style>
  .btn-box {
    width: 252px;
    height: 44px;
    font-size: 1.2rem;
  }
</style>



