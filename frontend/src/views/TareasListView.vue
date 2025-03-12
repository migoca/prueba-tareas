<template>  
    <div>
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols="8">
              <h2>Lista de Tareas</h2>
            </v-col>
            <v-col cols="4" align="right">
              <v-btn @click="openDialogCreateTarea()">Crear Tarea</v-btn>
            </v-col>
          </v-row>
          
        </v-card-title>    
        <v-card-text>
          <!-- Filters -->
          <v-row>           
            <v-col cols="3">
              <v-select 
                clearable
                label="Filtrar por Estado" 
                :items="estados" 
                item-text="nombre" 
                item-value="id" 
                v-model="filter_estados"
                @change="getTareas"                
                >                    
              </v-select>
            </v-col>
            <v-col cols="3">
              <v-menu
                    v-model="datepicker_menu_filter"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="filter_fecha_vencimiento"
                        label="Filtro por vencimiento"                    
                        readonly
                        v-bind="attrs"
                        v-on="on"
                        clearable
                        @click:clear="clearFilterVencimientoGetTareas"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="filter_fecha_vencimiento"
                        @input="datepicker_menu_filter = false"
                        @change="getTareas"
                    ></v-date-picker>
                </v-menu>
            </v-col>
          </v-row>
          <!-- // filters -->

          <v-data-table
            :headers="headers"
            :items="tareas"                  
            class="elevation-1">

            <template v-slot:[`item.familia`]="{ item }">              
                {{ getFamiliaName(item.familia) }}              
            </template>

            <template v-slot:[`item.actions`]="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="openDialogEditTarea(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                small
                @click="deleteTarea(item)"
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
                  <th>Familia</th>
                  <th>Título</th>
                  <th>Descripción</th>                  
                  <th>Estado</th>
                  <th>Fecha Creación</th>
                  <th>Fecha Vencimiento</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>                                
                <tr v-for="tarea in tareas" :key="tarea.id">
                  <td>{{ tarea.id }}</td>
                  <td>{{ getFamiliaName(tarea.familia) }}</td>
                  <td>{{ tarea.titulo }}</td>
                  <td>{{ tarea.descripcion }}</td>
                  <td>{{ tarea.estado }}</td>
                  <td>{{ tarea.fecha_creacion }}</td>
                  <td>{{ tarea.fecha_vencimiento }}</td>
                  <td>
                    <v-btn x-small @click="openDialogEditTarea(tarea)">Editar</v-btn> | 
                    <v-btn x-small @click="deleteTarea(tarea)">Eliminar</v-btn>
                  </td>
                </tr>
                
              </tbody>    
            </template>      
          </v-simple-table>
          -->
        </v-card-text>
      </v-card>
      
  
      <v-dialog v-model="dialog_edit_tarea" max-width="660">
        <v-card class="rounded-lg">      
          <v-card-title>
            <span class="text-h6 primary--text"><span v-if="current_tarea.id">Editar Tarea</span><span v-else>Crear Tarea</span></span>
          </v-card-title>      
          <v-divider></v-divider>
  
          <v-card-text class="pa-5">
            <v-form ref="form_tarea" v-model="validFormTarea">
                <v-text-field v-model="current_tarea.titulo" label="Titulo" outlined :rules="[v => !!v || 'Campo obligatorio']">            
                </v-text-field>
                <v-select 
                    :items="familias" 
                    v-model="current_tarea.familia" 
                    item-text="nombre" 
                    item-value="id" 
                    outlined 
                    label="Familia" 
                    :rules="[v => !!v || 'Campo obligatorio']">                
                </v-select>
                <v-textarea label="Descripción" v-model="current_tarea.descripcion" outlined :rules="[v => !!v || 'Campo obligatorio']"></v-textarea>
                <v-select label="Estado" :items="estados" item-text="nombre" item-value="id" v-model="current_tarea.estado" outlined>                    
                </v-select>
                <v-menu
                    v-model="datepicker_menu"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="current_tarea.fecha_vencimiento"
                        label="Fecha de vencimiento"                    
                        readonly
                        v-bind="attrs"
                        v-on="on"
                        outlined
                    ></v-text-field>
                    </template>
                    <v-date-picker
                        v-model="current_tarea.fecha_vencimiento"
                        @input="datepicker_menu = false"
                    ></v-date-picker>
                </v-menu>
            </v-form>

          </v-card-text>
  
          <v-card-actions>
            <v-btn @click="closeDialogCreateEditTarea()">Cancelar</v-btn>
            <v-btn @click="createEditTarea()" :disabled="!validFormTarea">Guardar</v-btn>
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
        tareas: [],
        familias: [],
        dialog_edit_tarea: false,
        current_tarea: {
          id: null,
          titulo: "",
          familia: null,
          descripcion: "",
          estado: "pendiente",
          fecha_vencimiento: null
        },
        datepicker_menu: false,
        datepicker_menu_filter: false,
        estados: [
            "pendiente", "en progreso", "completada"
        ],        
        validFormTarea: false,
        headers: [
          { text: 'ID', value: 'id' },
          { text: 'Familia', value: 'familia' },
          { text: 'Título', value: 'titulo', sortable: false },
          { text: 'Descripcion', value: 'descripcion', sortable: false },
          { text: 'Estado', value: 'estado' },
          { text: 'Fecha Creación', value: 'fecha_creacion', sortable: false },
          { text: 'Fecha Vencimiento', value: 'fecha_vencimiento'},
          { text: 'Aciones', value: 'actions', sortable: false },
        ],
        filter_estados: "",
        filter_fecha_vencimiento: null,  
      };
    },
    mounted() {
      this.getTareas();
      this.getFamilias();
    },
    methods: {
      async getTareas() {
        console.log("getTareas")
        let url = "tareas/"
        if (this.filter_estados) {
          url = url + "?estado=" + this.filter_estados
          if (this.filter_fecha_vencimiento) {
            url = url + "&fecha_vencimiento=" + this.filter_fecha_vencimiento
          }
        } else if (this.filter_fecha_vencimiento) {
          url = url + "?fecha_vencimiento=" + this.filter_fecha_vencimiento
        }
        const response = await api.get(url);        
        this.tareas = response.data;        
      },
      async clearFilterVencimientoGetTareas() {
        this.filter_fecha_vencimiento = null;
        this.getTareas()
      },
      async getFamilias() {
        const response = await api.get("familias/");
        this.familias = response.data;        
      },
      async createEditTarea() {
        let args = {
            titulo: this.current_tarea.titulo,
            familia:this.current_tarea.familia,
            descripcion: this.current_tarea.descripcion,
            estado: this.current_tarea.estado,
            fecha_vencimiento: this.current_tarea.fecha_vencimiento
        }
        if (this.current_tarea.id == null) {            
            await api.post("tareas/", args);
            this.getTareas();
            this.closeDialogCreateEditTarea()
        }
        else {
            await api.put(`tareas/${this.current_tarea.id}/`, args);
            this.getTareas();
            this.closeDialogCreateEditTarea()
        }
      },
      async deleteTarea(item) {
        await api.delete(`tareas/${item.id}/`);
        this.getTareas();
      },
      openDialogCreateTarea() {
        this.resetCurrentTarea();
        this.dialog_edit_tarea = true;
      },
      openDialogEditTarea(tarea) {
        this.current_tarea.id = tarea.id;
        this.current_tarea.titulo = tarea.titulo;
        this.current_tarea.familia = tarea.familia;
        this.current_tarea.descripcion = tarea.descripcion;
        this.current_tarea.estado = tarea.estado;
        this.current_tarea.fecha_vencimiento = tarea.fecha_vencimiento;
        this.dialog_edit_tarea = true;
      },
      closeDialogCreateEditTarea() {
        this.resetCurrentTarea();
        this.dialog_edit_tarea = false;
      },
      getFamiliaName(id) {        
        for (let x in this.familias) {
            if (this.familias[x].id == id) {
                return this.familias[x].nombre;
            }        
        }
        return id;
      },
      resetCurrentTarea() {
        this.current_tarea.id = null;
        this.current_tarea.titulo = "";
        this.current_tarea.familia = null;
        this.current_tarea.descripcion = "";
        this.current_tarea.fecha_vencimiento = null
      }
    },
    
  };
  </script>
  
  <style scoped>
  
  </style>