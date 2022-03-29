<template>
  <div class="cont" style="background-color:red">
    <headers/>
    <div class="principal">
      <div class="base">
        <h1>Login</h1>
      </div>
    </div>
    <footers/>
  </div>
</template>

<script>

export default {
  name: 'home',
}

</script>

<style lang="scss" scoped>
@import "@/layouts/variaveis.scss"; 

.cont{
  height: $conte;
 
}

.principal{
  background-color: #E5E5E5;
  position: absolute;
  top: $alturaHeader;
  bottom: $alturaFooter;
  background-color: #E5E5E5;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.base{
  background-color: #fff;
  width: 60%;
  height: 60%;
}

</style>