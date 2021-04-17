import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Interface';

  insertFile() {

    var properties = {
      "PartNumber": "",
      "PartName": "Bearing 8328-75 2000",
      "Description": ""
    }
    window.location.href = "fusion360://command=insert&file=" + encodeURIComponent("C:/Users/Misha/Desktop/DiplomProject/Bearing_GOST_8328-75_2000.f3d") +
      "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
      "&privateInfo=" + encodeURIComponent(this.setString()) +
      "&id=" + encodeURIComponent(Date.now().toString()); //id будет формироваться как номергоста_номердетали
      //это строго необходимо, т.к. при импорте детали, eсли id у деталей равны, он просто делает копию, и они связаны становятся
      //сейчас это тек.дата как временная заглушка
  }

  setString() {
    var str = (<HTMLInputElement>document.getElementById("d")).value + "/" +
      + (<HTMLInputElement>document.getElementById("D")).value + "/" +
      + (<HTMLInputElement>document.getElementById("B")).value + "/" +
      + (<HTMLInputElement>document.getElementById("_r")).value + "/" +
      + (<HTMLInputElement>document.getElementById("_r1")).value
    return str;
  }
}
