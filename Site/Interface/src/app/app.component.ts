import { Component, Type } from '@angular/core';
import { GostsService } from './services/gosts.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent { 
  title = 'Interface';
  gosts: any[];
  gost: any;
  TypeGosts: any[];
  constructor(private gostsService: GostsService){//получаем доступ к серверу

  }
//вроде как отвечает за инициализацию компонентк, эти данные подгружаются из бд сразу на страницу при ее открытии(это главнная страница)
  async ngOnInit(){
    await this.getGosts();
  }

   //получаем из сервиса данные, связанные с гостами
  async getGosts(){
    try{
      let gosts = this.gostsService.getAllGosts()//gosts получаем список всех гостов, которые есть на сервере
      this.gosts =  await gosts;
    }
    catch(err){
      console.error(err);
    }
  }
  //получаем данные о типе госта
  async getTypeGOSTS(gost){
    this.gost = gost;
    try{
      let TypeGosts = this.gostsService.getGostParams(gost.GOST,gost.ID)
      this.TypeGosts =  await TypeGosts;
    }
    catch(err){
      console.error(err);
    }
  }

  insertFile(TypeGost: any) {
    console.log(TypeGost);
    var properties = {
      "PartNumber": "",
      "PartName": this.gost.GOST + " " + TypeGost.NUMBER,
      "Description": ""
    }
    window.location.href = "fusion360://command=insert&file=" + encodeURIComponent(this.gost.MODEL_URL) +
      "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
      "&privateInfo=" + encodeURIComponent(this.setString(TypeGost)) +
      "&id=" + encodeURIComponent(this.gost.GOST + " " + TypeGost.NUMBER); //id будет формироваться как номергоста_номердетали
      //это строго необходимо, т.к. при импорте детали, eсли id у деталей равны, он просто делает копию, и они связаны становятся
      //сейчас это тек.дата как временная заглушка
  }

  setString(TypeGost) {
    var str = TypeGost._d + "/" +
      + TypeGost.D + "/" +
      + TypeGost.B + "/" +
      + TypeGost.r + "/" +
      + TypeGost.r1
    return str;
  }
}
