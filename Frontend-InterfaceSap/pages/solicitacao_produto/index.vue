// Solicitação de Produtos

<template>
  <div class="cont" style="background-color:red">
    <headers/>
    <div class="principal">
      <div class="base">
        <h1>Solicitação de Produtos</h1>
        <div class="centro">
        <section class="img">
            <img src="/logo.png">
        </section>

        <section class="campos">
            <input type="text" name="material" class="inputs" id="input1" placeholder="Material">
            <input type="text" name="quant" class="inputs" id="input2" placeholder="Quantidade">
            <input type="text" name="recebedor" class="inputs" id="input3" placeholder="Recebedor">
        </section>
        </div>
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
@import '@/pages/solicitacao_produto/solicitacao_produto.scss'
</style>