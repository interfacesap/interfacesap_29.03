<template>
    <footer class="rodape">
      <h4>© Robert Bosch Ltda. 2022, all rights reserved</h4>
    </footer>
</template>

<style lang="scss" scoped>
@import "@/layouts/variaveis.scss";

.rodape {
  position: absolute;
  bottom: 0;
  height: $alturaFooter;
  width: 100%;
  box-shadow: 0px -3px 10px 2px #b8b7b7;
  margin: 0;
  display: flex;
  justify-content: center;
  h4{
    display: flex;
    align-items: center;


 }
}
</style>