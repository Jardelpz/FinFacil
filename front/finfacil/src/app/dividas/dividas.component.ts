import { Component, OnInit } from '@angular/core';
import { DividaModel } from './dividas.model';
import { DividaService } from '../divida.service';
import { UserModel } from '../register/user.model';
import { UserService } from '../user.service';
import { RegisterComponent } from '../register/register.component';
import { ActivatedRoute } from '@angular/router'

@Component({
  selector: 'app-dividas',
  templateUrl: './dividas.component.html',
  styleUrls: ['./dividas.component.css']
})
export class DividasComponent implements OnInit {

  divida: DividaModel = new DividaModel()
  dividas: Array<any> = new Array()
  total: number  = 0
  msg: string = ""
  email: string
  constructor(private dividaService: DividaService, private router: ActivatedRoute) {
      this.email = this.router.snapshot.params['email']
   }

  ngOnInit() {
    this.calculaDivida()
    this.listarDividas(this.email)
  }

  calculaDivida(){
    this.dividaService.somaDivida(this.email).subscribe(d=>{
      this.total = d['total']
      this.msg = d['msg']
    })
  }

  addDivida(){
    this.dividaService.postDivida(this.divida, this.email).subscribe(d =>{
      // console.log("Sem retorno do id", d)
      this.divida = new DividaModel()
      this.listarDividas(this.email)
      this.calculaDivida()
    }, err => {
      console.log('Erro ao cadastrar divida', err)
    })
  }

  listarDividas(email: string){
    this.dividaService.listDividas(email).subscribe(divida =>{
      // console.log("LISTA DE DIVIDAS", divida)
      this.dividas = divida
    }, erro => {
      console.log("Erro ao listar dividas")
    })
  }

  pagarDivida(id: number){
    this.dividaService.pagarDivida(id).subscribe(() =>{
      console.log("Sucesso")
    }, err =>{
      console.log("Erro ao inserir")
    })
    this.listarDividas(this.email)
    this.calculaDivida()
  }
}
