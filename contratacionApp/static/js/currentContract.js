Vue.filter('formatDate', function (value) {
  if (value) {
    moment.locale("es");
    // return moment(String(value)).format('D MMMM YYYY, h:mm:ss a');
    return moment(String(value)).format('DD/MM/YYYY h:mm:ss a');
  }
}),
new Vue({
    el: "#starting",
    delimiters: ['${','}'],
    data: {
      contract: [],
      search_term: '',
      NUM_RESULTS: 5, // Numero de resultados por página
      pag: 1, // Página inicial
      
  },
  
  mounted: function() {
    this.getContract();
  },

  methods: {
      getContract: function() {
          let api_url = '/api/currentContract/currentMonth/';
          if(this.search_term !== '' || this.search_term !== null){
            api_url = '/api/currentContract/currentMonth/?search='+this.search_term;
          }
          this.$http.get(api_url)
              .then((response) => {
                this.contract = response.data;
              })
              .catch((err) => {
               console.log(err);
              })
      },
 }
});