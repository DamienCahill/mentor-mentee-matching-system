import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const ProfileCategorySelector = (props) => {
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [availableCategories, setAvailableCategories] = useState([]);
  useEffect(() => {
    fetchCategories();
  }, []);

  const handleAddCategoryClick = (e) => {
    let text = e.target.attributes[1].nodeValue;
    let newSelectedCategories = [].concat(selectedCategories);
    newSelectedCategories.push([e.target.id, text]);
    setAvailableCategories(availableCategories.filter((category) => category[0] != e.target.id));
    setSelectedCategories(newSelectedCategories);
    document.getElementById('selectedCategoryIds').value = newSelectedCategories.map(category => category[0]).join(',');
    console.log(document.getElementById('selectedCategoryIds').value);
  };

  const handleRemoveCategoryClick = (e) => {
    let newAvailableCategories = [].concat(availableCategories);
    let text = e.target.attributes[1].nodeValue;
    newAvailableCategories.push([e.target.id, text]);
    setSelectedCategories(selectedCategories.filter((category) => category[0] != e.target.id));
    let newVals = selectedCategories.filter((category) => category[0] != e.target.id);
    document.getElementById('selectedCategoryIds').value = newVals.map(category => category[0]).join(',');
    setAvailableCategories(newAvailableCategories);
    console.log(document.getElementById('selectedCategoryIds').value);
  };
  async function fetchCategories() {
    let allCategories = [];
    let selectedCategories = [];
    let canBeSelected = [];
    const allCategoriesRes = await fetch( `${props.apiUrl}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
      }
    });
    
    if( allCategoriesRes.ok ) {
      const json = await allCategoriesRes.json();
      allCategories = json;
    }

    if( ! allCategoriesRes.ok ) {
    }
    const mentorCategoriesRes = await fetch( `${props.apiUrl}/${props.mentorId}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
      }
    });

    if( mentorCategoriesRes.ok ) {
      const json = await mentorCategoriesRes.json();
      setSelectedCategories(json);
      selectedCategories = json;
      document.getElementById('selectedCategoryIds').value = json.map(category => category[0]).join(',');
      console.log(json);
    }

    if( ! mentorCategoriesRes.ok ) {
    }
    canBeSelected = allCategories.filter(item => !selectedCategories.some(otherItem => JSON.stringify(otherItem) === JSON.stringify(item)));
    setAvailableCategories(canBeSelected);

  }
return html`
  <input type=hidden id="selectedCategoryIds" name="selectedCategoryIds" value=""></input>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Selected Categories</h5>
        ${selectedCategories.map((categories, index) => (
          html`
            <a style="margin:3px;" class="btn btn-success" href="#">
              ${categories[1]} <i id=${categories[0]} name="${categories[1]}" class="fas fa-minus" onClick=${handleRemoveCategoryClick}></i>
            </a>
          `
        ))}
    </div>
  </div>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Available Categories</h5>
        ${availableCategories.map((categories, index) => (
          html`
            <a style="margin:3px;" class="btn btn-primary" href="#">
              ${categories[1]} <i id=${categories[0]} name="${categories[1]}" class="fas fa-plus" onClick=${handleAddCategoryClick}></i>
            </a><br/>
          `
        ))}
    </div>
  </div>
`;

};
export { ProfileCategorySelector };