import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BeerCreateComponent } from './beer-create.component';

describe('BeerCreateComponent', () => {
  let component: BeerCreateComponent;
  let fixture: ComponentFixture<BeerCreateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BeerCreateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BeerCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
