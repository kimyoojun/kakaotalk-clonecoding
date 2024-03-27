<script>
  export let mySpeechBubble = ""
  export let chatClass = ""
</script>

<div class="{chatClass}-wrap">
  <div class={chatClass}>
    {mySpeechBubble}
  </div>
</div>

<style>
  .mychat-wrap {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: flex-end;
  }

  .mychat {
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

  .userchat-wrap {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: flex-start;
  }

  .userchat {
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
  }

</style>