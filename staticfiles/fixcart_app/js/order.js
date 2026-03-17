document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (toggle) {
        toggle.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }


    /* IMAGE UPLOAD WITH REMOVE OPTION */

    const imageUpload = document.getElementById("imageUpload");
    const preview = document.getElementById("imagePreview");

    let selectedFiles = [];


    if (imageUpload) {

        imageUpload.addEventListener("change", function () {

            const files = Array.from(this.files);

            files.forEach(file => {

                selectedFiles.push(file);

                const reader = new FileReader();

                reader.onload = function (e) {

                    const imageBox = document.createElement("div");
                    imageBox.classList.add("preview-box");

                    const img = document.createElement("img");
                    img.src = e.target.result;

                    const removeBtn = document.createElement("button");
                    removeBtn.innerText = "✕";
                    removeBtn.classList.add("remove-btn");

                    removeBtn.onclick = function () {

                        imageBox.remove();

                        selectedFiles = selectedFiles.filter(f => f !== file);

                        updateInputFiles();

                    };

                    imageBox.appendChild(img);
                    imageBox.appendChild(removeBtn);

                    preview.appendChild(imageBox);

                };

                reader.readAsDataURL(file);

            });

            updateInputFiles();

        });

    }


    /* UPDATE FILE INPUT */

    function updateInputFiles() {

        const dataTransfer = new DataTransfer();

        selectedFiles.forEach(file => {
            dataTransfer.items.add(file);
        });

        imageUpload.files = dataTransfer.files;

    }

});