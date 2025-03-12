<template>  
  <div>
    <v-card>
      <v-card-title>
        <v-row>
          <v-col cols="8">
            <h2>Lista de Familias</h2>
          </v-col>
          <v-col cols="4" align="right">
            <v-btn @click="openDialogCreateFamilia()">Crear Familia</v-btn>
          </v-col>
        </v-row>
        
      </v-card-title>    
      <v-card-text>
        <v-data-table
            :headers="headers"
            :items="familias"                  
            class="elevation-1">            

            <template v-slot:[`item.actions`]="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="openDialogEditFamilia(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                small
                @click="deleteFamilia(item.id)"
              >
                mdi-delete
              </v-icon>
            </template>
          </v-data-table>
        <!--
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th>ID</th>
                <th >Nombre</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="familia in familias" :key="familia.id">
                <td>{{ familia.id }}</td>
                <td>{{ familia.nombre }}</td>
                <td>
                  <v-icon
                    small
                    class="mr-2"
                    @click="openDialogEditFamilia(familia)"
                  >
                    mdi-pencil
                  </v-icon>
                  <v-icon
                    small
                    @click="deleteFamilia(familia.id)"
                  >
                    mdi-delete
                  </v-icon>
                  
                </td>
              </tr>
            </tbody>    
          </template>      
        </v-simple-table>
        -->
      </v-card-text>
    </v-card>
    

    <v-dialog v-model="dialog_edit_familia" max-width="660">
      <v-card class="rounded-lg">      
        <v-card-title>
          <span class="text-h6 primary--text"><span v-if="current_familia.id">Editar Familia</span><span v-else>Crear Familia</span></span>
        </v-card-title>      
        <v-divider></v-divider>

        <v-card-text class="pa-5">
          <v-form ref="form_familia" v-model="validFormFamilia">
            <v-text-field v-model="current_familia.nombre" label="Nombre" outlined :rules="[v => !!v || 'Campo obligatorio']">            
            </v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn @click="closeDialogCreateEditFamilia()">Cancelar</v-btn>
          <v-btn @click="createEditFamilia()" :disabled="!validFormFamilia">Guardar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "../api/api";

export default {
  data() {
    return { 
      familias: [],
      dialog_edit_familia: false,
      current_familia: {
        id: null,
        nombre: ""
      },
      validFormFamilia: false,
      headers: [
          { text: 'ID', value: 'id' },
          { text: 'Nombre', value: 'nombre' },
          { text: 'Aciones', value: 'actions', sortable: false },
      ]

    };
  },
  mounted() {
    this.getFamilias();
  },
  methods: {
    async getFamilias() {
      const response = await api.get("familias/");      
      this.familias = response.data;
    },
    async createEditFamilia() {      
      if (this.current_familia.id == null) {
        await api.post("familias/", { nombre: this.current_familia.nombre});
        this.getFamilias();
        this.closeDialogCreateEditFamilia()
      }
      else {
        await api.put(`familias/${this.current_familia.id}/`, { nombre: this.current_familia.nombre });
        this.getFamilias();
        this.closeDialogCreateEditFamilia()
      }
    },
    async deleteFamilia(id) {
      await api.delete(`familias/${id}/`);
      this.getFamilias();
    },
    openDialogCreateFamilia() {
      this.current_familia.id = null;
      this.current_familia.nombre = "";
      this.dialog_edit_familia = true;
    },
    openDialogEditFamilia(familia) {
      this.current_familia.id = familia.id;
      this.current_familia.nombre = familia.nombre;
      this.dialog_edit_familia = true;
    },
    closeDialogCreateEditFamilia() {
      this.current_familia.id = null;
      this.current_familia.nombre = "";
      this.dialog_edit_familia = false;
    }
  },
  
};
</script>

<style scoped>

</style>