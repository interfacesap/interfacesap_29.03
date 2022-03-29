// Sucata

<template>
  <div class="cont" style="background-color:red">
    <headers/>
    <div class="principal">
      <div class="base">
        <h1>Descarte Sucata</h1>
        <input type="text" name="denominacao" class="inputs" id="input1" placeholder="Denominação">
        <input type="text" name="codigo" class="inputs" id="input2" placeholder="Codigo">
        <input type="text" name="quant" class="inputs" id="input3" placeholder="Quantidade">
        <input type="text" name="descricao" class="inputs" id="input4" placeholder="Descricao">
        <button> Enviar </button>
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
@import '@/pages/sucata/sucata.scss'
</style>