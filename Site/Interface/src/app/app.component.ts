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
      "PartNumber": "21345",
      "PartName": "Bearing 8328-75 2000",
      "Description": this.setString()
    }
    window.location.href = "fusion360://command=insert&file=" + encodeURIComponent("C:/Users/Misha/Desktop/DiplomProject/Bearing_GOST_8328-75_2000.f3d") +
      "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
      "&privateInfo=" + encodeURIComponent(this.setString()) +
      "&id=" + encodeURIComponent("gege");
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
