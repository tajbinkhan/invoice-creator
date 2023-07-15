$(".date-picker").datepicker({
	autoclose: true,
	orientation: "bottom",
	format: "dd/mm/yyyy",
});

$(document).ready(function () {
	$(".currencypicker ").select2({
		placeholder: "Select a client",
		minimumResultsForSearch: Infinity,
	});

	for (var i = 0; i < currentFormCount; i++) {
		$(`#id_bill_goods-${i}-unit`).select2({
			minimumResultsForSearch: Infinity,
		});
	}
});

// Get all delete buttons
var deleteButtons = document.querySelectorAll(".form-check-label");
for (var i = 0; i < deleteButtons.length; i++) {
	const ignoreValue = deleteButtons[i].getAttribute("for");
	if (ignoreValue != "id_bill_goods-__prefix__-DELETE") {
		deleteButtons[i].setAttribute("class", "btn btn-danger form-check-label");
	}
}

// Adding Goods Using JavaScript
const addMoreBtn = document.getElementById("add-goods");
const totalNewForms = document.getElementById("id_bill_goods-TOTAL_FORMS");
const element = document.getElementById("instruction");

const currentGoodsForms = document.getElementsByClassName("goods-list");
const currentFormCount = currentGoodsForms.length;

// Add click event listener to each delete button
deleteButtons.forEach(function (button) {
	button.addEventListener("click", function () {
		var goodsList = this.closest(".goods-list");
		goodsList.style.display = "none";
	});
});

if (currentFormCount > 0) {
	element.style.display = "none";
}

addMoreBtn.addEventListener("click", (event) => {
	if (event) {
		event.preventDefault();
	}

	if (element) {
		element.style.display = "none";
	}

	const formCopyTarget = document.getElementById("goods-form");
	const copyEmptyFormEl = document.getElementById("empty-form").cloneNode(true);
	const updatedFormCount = currentGoodsForms.length;

	copyEmptyFormEl.setAttribute(
		"class",
		"row goods-list dynamic-bill_goods"
	);
	copyEmptyFormEl.setAttribute("id", `form-${updatedFormCount}`);

	const regex = new RegExp("__prefix__", "g");
	copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(
		regex,
		updatedFormCount
	);
	totalNewForms.setAttribute("value", updatedFormCount + 1);
	formCopyTarget.append(copyEmptyFormEl);

	const colorElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-color`
	);
	const countElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-count`
	);
	const qtyElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-quantity`
	);
	const unitElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-unit`
	);
	const unitPriceElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-unit_price`
	);
	const deleteElement = document.getElementById(
		`div_id_bill_goods-${updatedFormCount}-DELETE`
	);

	colorElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3 mb-3");
	countElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3 mb-3");
	qtyElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3 mb-3");
	unitElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3 mb-3");
	unitPriceElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3 mb-3");
	deleteElement.setAttribute("class", "col-sm-12 col-md-6 col-lg-3");

	var forAttributeValue = `id_bill_goods-${updatedFormCount}-DELETE`;
	var labelElement = document.querySelector(
		'label[for="' + forAttributeValue + '"]'
	);
	labelElement.style.display = "none";

	$(`#id_bill_goods-${updatedFormCount}-unit`).select2({
		minimumResultsForSearch: Infinity,
	});

	const deleteBtn = document.createElement("button");
	deleteBtn.innerHTML = "Delete";
	deleteBtn.classList.add("btn", "btn-danger");
	deleteBtn.addEventListener("click", () => {
		const forms = document.getElementsByClassName("goods-list");
		const totalFormsInput = document.getElementById(
			"id_bill_goods-TOTAL_FORMS"
		);
		totalFormsInput.value = forms.length - 1;

		if (forms.length - 1 === 0) {
			element.style.display = "block";
		} else {
			element.style.display = "none";
		}

		var removedId = copyEmptyFormEl;
		var convertToArray = Array.from(forms);
		var removedIndex = convertToArray.indexOf(removedId);
		copyEmptyFormEl.remove();
		if (removedIndex !== -1) {
			convertToArray.splice(removedIndex, 1);
			for (var i = removedIndex; i < convertToArray.length; i++) {
				var updatedId = convertToArray[i].id.replace(/\d+/, i);
				convertToArray[i].id = updatedId;

				var childNodes = convertToArray[i].children;
				var childNodesArray = Array.from(childNodes);

				var select2Span = Array.from(
					document.getElementsByClassName("select2-selection__rendered")
				);
				var updatedSelect2Span = select2Span[2].id.replace(/-\d+-/, `-${i}-`);
				select2Span[2].id = updatedSelect2Span;

				for (var j = 0; j < childNodesArray.length; j++) {
					var inititalChildId = childNodesArray[j].getAttribute("id");
					var inititalChildName = childNodesArray[j].getAttribute("name");

					if (inititalChildId !== null) {
						var modifiedChildId = childNodesArray[j]
							.getAttribute("id")
							.replace(/\d+/, i);
						childNodesArray[j].setAttribute("id", modifiedChildId);

						var newInitialIdChildArray = Array.from(
							document.getElementById(childNodesArray[j].getAttribute("id"))
								.children
						);

						newInitialIdChildArray.forEach(function (newElement) {
							if (newElement.getAttribute("id") !== null) {
								var modifiedChildrenId = newElement
									.getAttribute("id")
									.replace(/\d+/, i);
								newElement.setAttribute("id", modifiedChildrenId);

								if (
									newElement.getAttribute("id") ===
									`id_bill_goods-${i}-unit`
								) {
									$(`#id_bill_goods-${i}-unit`).select2({
										minimumResultsForSearch: Infinity,
									});
								}
							}

							if (newElement.getAttribute("name") !== null) {
								var modifiedChildrenName = newElement
									.getAttribute("name")
									.replace(/\d+/, i);
								newElement.setAttribute("name", modifiedChildrenName);
							}

							if (newElement.getAttribute("for") !== null) {
								var modifiedChildrenFor = newElement
									.getAttribute("for")
									.replace(/\d+/, i);
								newElement.setAttribute("for", modifiedChildrenFor);
							}
						});
					}

					if (inititalChildName !== null) {
						var modifiedChildName = childNodesArray[j]
							.getAttribute("name")
							.replace(/\d+/, i);
						childNodesArray[j].setAttribute("name", modifiedChildName);
					}
				}

				var getClassName = Array.from(
					Array.from(
						Array.from(document.querySelectorAll(`#${convertToArray[i].id}`))[0]
							.children
					)[7].children
				)[0];
				var getClassNameChildren = Array.from(
					Array.from(
						Array.from(document.querySelectorAll(`#${convertToArray[i].id}`))[0]
							.children
					)[7].children
				)[0].children;

				var updatedGetClassName = getClassName.id.replace(/\d+/, i);
				var updatedGetClassNameId = getClassNameChildren[0]
					.getAttribute("id")
					.replace(/\d+/, i);
				var updatedGetClassNameName = getClassNameChildren[0]
					.getAttribute("name")
					.replace(/\d+/, i);
				var updatedGetClassNameFor = getClassNameChildren[1]
					.getAttribute("for")
					.replace(/\d+/, i);

				getClassName.id = updatedGetClassName;
				getClassNameChildren[0].setAttribute("id", updatedGetClassNameId);
				getClassNameChildren[0].setAttribute("name", updatedGetClassNameName);
				getClassNameChildren[1].setAttribute("for", updatedGetClassNameFor);
			}
		}
	});

	deleteElement.appendChild(deleteBtn);
});
