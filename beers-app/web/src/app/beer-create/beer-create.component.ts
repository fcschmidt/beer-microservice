import { Component, OnInit } from '@angular/core';
import { Location } from "@angular/common";
// import { FormGroup, FormControl } from "@angular/forms";



@Component({
  selector: 'app-beer-create',
  templateUrl: './beer-create.component.html',
  styleUrls: ['./beer-create.component.css']
})
export class BeerCreateComponent implements OnInit {


  constructor(
    private location: Location,
  ) { }

  ngOnInit() {
  }


  goBack(): void {
    this.location.back();
  }
}
