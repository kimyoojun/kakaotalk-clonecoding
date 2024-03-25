<script>
  export let mySpeechBubble = ""
</script>

<div class="speech-wrap">
  <div class="speech">
    {mySpeechBubble}
  </div>
</div>

<style>
  .speech-wrap {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: flex-end;
  }

  .speech {
    background-color: #fef01b;
    margin-right: 20px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: auto;
    height: auto;
    padding: 8px 8px;
    border-radius: 4px;
  }

  /* .speech-wrap {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: flex-start;
  }


  .speech {
    background-color: #ffffff;
    margin-left: 20px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: auto;
    height: auto;
    padding: 8px 8px;
    border-radius: 4px;
  } */

</style>